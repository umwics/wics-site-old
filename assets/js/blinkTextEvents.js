const START_TEXT_CONTENT_INDEX = [
1,
1,
1
];
// For blinking text in home page
const HOME_TEXT_CONTENT = [
    "Join these Events!",
    "It is fun!",
    "Games and Foods!"
]

intervalStart = setInterval(() => {textManipulate(1,HOME_TEXT_CONTENT,START_TEXT_CONTENT_INDEX)}, 70);