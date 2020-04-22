const START_TEXT_CONTENT_INDEX = [
30,
1,
1
];
// For blinking text in home page
const HOME_TEXT_CONTENT = [
    "This Slack is where we discuss upcoming events",
    "This Slack is where we discuss current news",
    "To connect with other members!"
]

intervalStart = setInterval(() => {textManipulate(1,HOME_TEXT_CONTENT,START_TEXT_CONTENT_INDEX)}, 70);