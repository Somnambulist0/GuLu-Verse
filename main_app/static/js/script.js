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
        if (!answers.some(ans => ans.question === question)) {
            answers.push({ question: question, answer: answer });
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
    // Collect the data you need to send to the server
    const requestData = {
        mood: answers.find(answer => answer.question === 'q1')?.answer,
        classic: answers.find(answer => answer.question === 'q2')?.answer,
        noisy: answers.find(answer => answer.question === 'q3')?.answer,
        reality: answers.find(answer => answer.question === 'q4')?.answer,
        alone: answers.find(answer => answer.question === 'q5')?.answer

    };

    // Send the data to the Django backend 
    fetch('/recommend_movies/', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/display_recommendations/';
        } else {
            throw new Error('Network response was not ok.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


