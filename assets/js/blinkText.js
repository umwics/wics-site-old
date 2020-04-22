let textContentIndex = 0; // the current index of the sentence being processed
let letterIndex = 2; // the part of the current letter that the current sentence is being processed
let blinkingTextElement = document.querySelector(".blink-text");
let intervalStart; // handles the setInterval variable where timing is required

/*
Takes an argument where the argument specifies if the current process is deleting text or 
typing text.
This function will start the process of typing text or deleting text for the animation of 
typeWriter Effect.

@param manipulateType - integer value +1 or -1 where +1 refers to typing text and -1 refers to deleting text

*/
function textManipulate(manipulateType,TEXT_CONTENT,START_TEXT_CONTENT_INDEX) {
    let currentSentence = TEXT_CONTENT[textContentIndex].substring(0, letterIndex);
    blinkingTextElement.innerHTML = currentSentence;
    letterIndex += manipulateType;
    let endSentenceLength = START_TEXT_CONTENT_INDEX[textContentIndex]+1;
    // if we are typing text, then the end process will occur when the sentence
    // this function is typing equals to the full sentence
    // if we are deleting text, the end process will occur when the sentence we are typing
    // reaches empty
    if (manipulateType === 1) {
        endSentenceLength = TEXT_CONTENT[textContentIndex].length;
    }

    // when we have reach the end of the sentence we will start the delete process
    if (currentSentence.length === endSentenceLength) {

        // change the text
        if (manipulateType === -1) {
        textContentIndex ++;
        if (textContentIndex > TEXT_CONTENT.length - 1)
            textContentIndex = 0;
        }
        
        clearInterval(intervalStart);
        setTimeout(() => {
            // manipulateType * -1 will change typing to deleting and vice versa
            intervalStart = setInterval(() => {
                textManipulate(manipulateType * -1,TEXT_CONTENT,START_TEXT_CONTENT_INDEX)
            }, 50); 
        }, 1000)
        
    }
}