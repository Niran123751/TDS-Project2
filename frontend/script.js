const API_URL = "https://your-render-backend-url.onrender.com";  // Replace with actual deployed backend URL

async function generateQuiz() {
    const topic = document.getElementById("topicInput").value;

    const response = await fetch(`${API_URL}/quiz`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic })
    });

    const data = await response.json();
    displayQuiz(data.questions);
}

function displayQuiz(questions) {
    document.getElementById("quizContainer").classList.remove("hidden");

    const questionDiv = document.getElementById("questions");
    questionDiv.innerHTML = "";

    questions.forEach((q, index) => {
        questionDiv.innerHTML += `
        <div class="question-block">
            <p><strong>${index + 1}. ${q.question}</strong></p>
            ${q.options.map(opt => `
                <label><input type="radio" name="q${index}" value="${opt}"> ${opt}</label><br>
            `).join("")}
        </div>`;
    });
}

async function submitAnswers() {
    const answers = [];
    document.querySelectorAll(".question-block").forEach((block, index) => {
        const selected = document.querySelector(`input[name="q${index}"]:checked`);
        answers.push(selected ? selected.value : null);
    });

    const response = await fetch(`${API_URL}/evaluate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answers })
    });

    const result = await response.json();
    document.getElementById("resultContainer").classList.remove("hidden");
    document.getElementById("score").textContent = `${result.score} / ${answers.length}`;
}
