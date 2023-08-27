const textContainers = document.querySelectorAll(".albumBio");

textContainers.forEach((textContainer) => {
    const textLength = textContainer.textContent.length;

    let fontSize;

    if (textLength > 500) {
        fontSize = '10px';
    } else if (textLength > 300) {
        fontSize = '11px';
    } else if (textLength > 50) {
        fontSize = '12px'
    } else {
        fontSize = '14'
    }

    textContainer.style.fontSize = fontSize;
});
