const START_TEXT_CONTENT_INDEX = [
1,
1
];
// For blinking text in home page
const HOME_TEXT_CONTENT = [
    "Time to Learning then sharing",
    "This is the best place to begin!"
]

intervalStart = setInterval(() => {textManipulate(1,HOME_TEXT_CONTENT,START_TEXT_CONTENT_INDEX)}, 70);