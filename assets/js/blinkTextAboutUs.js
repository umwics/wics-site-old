const START_TEXT_CONTENT_INDEX = [
1,
1
];
// For blinking text in home page
const HOME_TEXT_CONTENT = [
    "We will support you in WICS",
    "All are welcome to join WICS!"
]

intervalStart = setInterval(() => {textManipulate(1,HOME_TEXT_CONTENT,START_TEXT_CONTENT_INDEX)}, 70);