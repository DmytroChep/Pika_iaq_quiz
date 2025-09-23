const socket = io(); 

function ReturnLastElement(array){
    return array[array.length - 1]
}

const Username = document.querySelector(".username").textContent;
const QuizId = ReturnLastElement(window.location.href.split("/"))



socket.emit('joinQuiz', {
    user: `${Username}`,
    quiz: `${QuizId}`
});