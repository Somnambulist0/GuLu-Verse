const bubbles = document.querySelectorAll('.talk-bubble');
let answers = [];

window.addEventListener('scroll', function() {
    let st = window.scrollY;
    let windowHeight = window.innerHeight;
    let docHeight = document.documentElement.scrollHeight;

    bubbles.forEach(bubble => {
        let bubblePosition = bubble.getAttribute('data-position') * docHeight;

        if (st + windowHeight > bubblePosition && st + (windowHeight / 2) < bubblePosition && !answers.includes(bubble.getAttribute('data-question'))) {
            bubble.style.display = 'block';
        } else {
            bubble.style.display = 'none';
        }
    });
});

document.body.addEventListener('click', function(event) {
    if (event.target.tagName.toLowerCase() === 'button' && event.target.hasAttribute('data-answer')) {
        const answer = event.target.getAttribute('data-answer');
        const question = event.target.closest('.talk-bubble').getAttribute('data-question');

        if (!answers.includes(question)) {
            answers.push(question);
        }

        const bubbleButtons = event.target.closest('.talk-bubble').querySelectorAll('button');

        bubbleButtons.forEach(button => button.classList.remove('selected-option'));

        event.target.classList.add('selected-option');

        if (answers.length === bubbles.length) {
            displayRecommendation();
        }
    }
});

function displayRecommendation() {
    alert("Based on your answers, we recommend you to have a relaxing day and enjoy some music!");
}


