const START_TEXT_CONTENT_INDEX = [
8,
8
];
// For blinking text in home page
const HOME_TEXT_CONTENT = [
    "You will find fantastic opportunity here",
    "You will be suppurted in Wics"
]

intervalStart = setInterval(() => {textManipulate(1,HOME_TEXT_CONTENT,START_TEXT_CONTENT_INDEX)}, 70);