let currentQuestion = -1;
let answers = [];

const questions = [
    {
        title: "How do you feel today?",
        options: ["Happy", "Sad", "Neutral"]
    },
    {
        title: "Do you prefer indoor or outdoor activities?",
        options: ["Indoor", "Outdoor"]
    },
    {
        title: "How many hours of free time do you have today?",
        options: ["1-2 hours", "3-4 hours", "More than 4 hours"]
    }
];

function nextQuestion() {
    currentQuestion++; 
    if (currentQuestion < questions.length) {
        const question = questions[currentQuestion];
        let optionsHtml = "";

        question.options.forEach((option, index) => {
            optionsHtml += `<button onclick="selectOption(${index})">${option}</button><br>`;
        });

        document.querySelector('.window').innerHTML = `
            <h1 class="title">${question.title}</h1>
            ${optionsHtml}
        `;
    } else {
        displayResult();
    }
}

function selectOption(index) {
    answers.push(index);
    nextQuestion();
}

function displayResult() {
    document.querySelector('.window').innerHTML = `
        <p>Based on your answers, we recommend you to have a relaxing day and enjoy some music!</p>
    `;
}
