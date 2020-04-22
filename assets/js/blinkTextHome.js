const START_TEXT_CONTENT_INDEX = [
6,
6,
2,
2,
2,
];
// For blinking text in home page
const HOME_TEXT_CONTENT = [
    "We are WICS, all are welcome to join!",
    "We are women in computer science",
    "We are problem solvers and developers",
    "We support women in technology",
    "We support equality in STEM"
]

intervalStart = setInterval(() => {textManipulate(1,HOME_TEXT_CONTENT,START_TEXT_CONTENT_INDEX)}, 50);