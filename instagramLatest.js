// Simple node script with no deps to fetch the most recent post from instagram

const https = require("https");
const fs = require("fs");

const fetch = (url, opts = {}) => {
  return new Promise((resolve, reject) =>
    https
      .get(url, opts, res => {
        const { statusCode, headers } = res;
        const contentType = headers["content-type"];

        let error;
        if (statusCode !== 200) {
          error = new Error("Request Failed.\n" + `Status Code: ${statusCode}`);
        } else if (!/^application\/json/.test(contentType)) {
          error = new Error(
            "Invalid content-type.\n" + `Expected application/json but received ${contentType}`
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
            const parsedData = JSON.parse(rawData);
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
  return fetch(`https://www.instagram.com/${user}/?__a=1`);
};

const fetchRecentShortId = user => {
  return fetchRecent(user).then(data => {
    if (data && data.graphql && data.graphql.user) {
      const user = data.graphql.user;
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

const fetchEmbed = (shortCode, hideCaption = false, maxWidth = 540) => {
  return fetch(
    `https://api.instagram.com/oembed/?url=https://www.instagram.com/p/${shortCode}/&hidecaption=${
      hideCaption ? 1 : 0
    }&maxwidth=${maxWidth}`
  );
};

const saveInstagramEmbed = async user => {
  const shortCode = await fetchRecentShortId(user);

  if (shortCode) {
    const embed = await fetchEmbed(shortCode);

    if (embed && embed.html) {
      fs.writeFile("./_includes/instagram-latest.html", embed.html, err => {
        if (err) {
          console.error(err);
          return;
        }
        console.log("Successfully grabbed latest instagram post");
      });
    }
  }
};

saveInstagramEmbed("umwics");
