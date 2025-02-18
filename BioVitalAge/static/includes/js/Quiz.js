/*  -----------------------------------------------------------------------------------------------
    Quiz
--------------------------------------------------------------------------------------------------- */
const questionsContainer = document.getElementById("quiz-container");
const questions = questionsContainer.querySelectorAll(".question");
const nextBtn = document.getElementById("next-btn");
const prevBtn = document.getElementById("prev-btn");
const pagination = document.getElementById("pagination");

let currentQuestionIndex = 0;

// Funzione per aggiornare la domanda attiva
function updateQuestion(index) {
  questions[currentQuestionIndex].classList.remove("active");
  currentQuestionIndex = index;
  questions[currentQuestionIndex].classList.add("active");
  updatePagination();
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

// Funzione per aggiornare la paginazione
function updatePagination() {
  const paginationButtons = pagination.querySelectorAll(".pagination-btn");
  paginationButtons.forEach((btn, index) => {
    if (index === currentQuestionIndex) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });
}

// Funzione per generare i pulsanti della paginazione
function createPagination() {
  pagination.innerHTML = "";

  questions.forEach((_, index) => {
    const button = document.createElement("button");
    button.classList.add("pagination-btn");
    button.textContent = index + 1;
    button.type = "button"; // Aggiunto per evitare l'invio del form
    button.addEventListener("click", () => updateQuestion(index));
    pagination.appendChild(button);
  });
}


// Gestori per i pulsanti successivo e precedente
function nextAnswer() {
  if (currentQuestionIndex < questions.length - 1) {
    updateQuestion(currentQuestionIndex + 1);
  }
}

function prevAnswer() {
  if (currentQuestionIndex > 0) {
    updateQuestion(currentQuestionIndex - 1);
  }
}

nextBtn.addEventListener("click", nextAnswer);
prevBtn.addEventListener("click", prevAnswer);

// Inizializzazione
createPagination();
updatePagination();

const submitBtn = document.getElementById("submit-btn");

function checkLastQuestion() {
  const lastQuestion = document.querySelector(".tableRow"); 
  const inputs = lastQuestion.querySelectorAll("input[type='radio'], input[type='text']");
  
  const allFilled = Array.from(inputs).some((input) => input.checked); 

  submitBtn.disabled = !allFilled;
}

document.querySelectorAll("input[name='Sarc_5']").forEach(input => {
  input.addEventListener("change", checkLastQuestion);
});


function handleCheckboxSelection() {
  const checkboxes =
    questions[currentQuestionIndex].querySelectorAll(".answer");
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      checkboxes.forEach((box) => {
        if (box !== checkbox) box.checked = false;
      });
      checkLastQuestion();
    });
  });
}

function updateQuestion(index) {
  questions[currentQuestionIndex].classList.remove("active");
  currentQuestionIndex = index;
  questions[currentQuestionIndex].classList.add("active");
  updatePagination();
  checkLastQuestion();
  if (currentQuestionIndex === questions.length - 1) {
    handleCheckboxSelection();
  }
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

// Aggiorna la funzione nextAnswer per includere il controllo
function nextAnswer() {
  if (currentQuestionIndex < questions.length - 1) {
    updateQuestion(currentQuestionIndex + 1);
  }
}

// Inizializzazione
createPagination();
updatePagination();
handleCheckboxSelection();


document.querySelectorAll("input[type='radio'], input[type='text']").forEach((input) => {
  input.addEventListener("input", checkLastQuestion);
});





