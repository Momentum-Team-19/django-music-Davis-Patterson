const textContainers = document.querySelectorAll(".albumBio");

textContainers.forEach((textContainer) => {
    const textLength = textContainer.textContent.length;

    let fontSize;

    if (textLength > 250) {
        fontSize = '10px';
    } else if (textLength > 100) {
        fontSize = '12px';
    } else {
        fontSize = '14px'
    }

    textContainer.style.fontSize = fontSize;
});