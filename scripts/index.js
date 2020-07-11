const fs = require("fs");
const path = require("path");

const taskRunners = fs
    .readdirSync(__dirname, { withFileTypes: true })
    .filter(dirent => dirent.name !== "index.js" && dirent.isFile())
    .map(dirent => require(path.join(__dirname, dirent.name)));
