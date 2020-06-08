// Simple node script with no deps to fetch the most recent post from instagram
// Good resource if you don't want to use an instagram access token https://stackoverflow.com/questions/17373886/how-can-i-get-a-users-media-from-instagram-without-authenticating-as-a-user

const https = require("https");
const fs = require("fs");

const fetch = (url, opts = {}) => {
    return new Promise((resolve, reject) =>
        https
            .get(url, opts, res => {
                const { statusCode, headers } = res;
                const contentType = headers["content-type"];
                const isJSON = /^application\/json/.test(contentType);

                let error;
                if (statusCode !== 200) {
                    error = new Error(
                        `Request Failed.\n Status Code: ${statusCode}\n Headers: ${JSON.stringify(
                            headers
                        )}`
                    );
                }
                if (error) {
                    // Consume response data to free up memory
                    res.resume();

                    reject(error);
                }

                res.setEncoding("utf8");
                let rawData = "";
                res.on("data", chunk => {
                    rawData += chunk;
                });
                res.on("end", () => {
                    try {
                        const parsedData = isJSON ? JSON.parse(rawData) : rawData;
                        resolve(parsedData);
                    } catch (e) {
                        reject(e);
                    }
                });
            })
            .on("error", e => {
                reject(e);
            })
    );
};

const fetchRecent = user => {
    //   const instagramURL = `https://www.instagram.com/${user}/?__a=1`;

    const queryId = 17888483320059182; // constant, may be changed in the future
    const authorId = user;
    const instagramURL = `https://www.instagram.com/graphql/query/?query_id=${queryId}&variables={"id":"${authorId}","first":5,"after":null}`;

    return fetch(encodeURI(instagramURL));
};

const fetchRecentShortId = user => {
    return fetchRecent(user).then(data => {
        if (data && ((data.data && data.data.user) || (data.graphql && data.graphql.user))) {
            const user = data.data ? data.data.user : data.graphql.user;
            const timeline = user.edge_owner_to_timeline_media;
            const postExists = timeline && timeline.count > 0;
            if (postExists) {
                const post = timeline.edges[0].node;
                const shortCode = post.shortcode;

                if (shortCode) {
                    return shortCode;
                } else {
                    throw new Error("Could not find shortCode");
                }
            } else {
                throw new Error("No posts exist");
            }
        } else {
            throw new Error("Request returned null data");
        }
    });
};

const fetchEmbed = (
    shortCode,
    { hideCaption = false, maxWidth = 540, omitscript = false } = {}
) => {
    return fetch(
        `https://api.instagram.com/oembed/?url=https://www.instagram.com/p/${shortCode}/&hidecaption=${
            hideCaption ? 1 : 0
        }&maxwidth=${maxWidth}&omitscript=${omitscript}`
    );
};

const instaEmbed = `{% asset dist/instagramEmbed.min.js async %}`;

const saveInstagramEmbed = async user => {
    try {
        const shortCode = await fetchRecentShortId(user);

        if (shortCode) {
            const embed = await fetchEmbed(shortCode, { omitscript: true });

            if (embed && embed.html) {
                fs.writeFile("./_includes/instagram-latest.html", embed.html + instaEmbed, err => {
                    if (err) {
                        console.error(err);
                        return;
                    }
                    console.log("Successfully grabbed latest instagram post");
                });
            }
        }
    } catch (e) {
        console.error(e);
    }
};

// saveInstagramEmbed("umwics");
saveInstagramEmbed(8347229779); // userId of umwics
