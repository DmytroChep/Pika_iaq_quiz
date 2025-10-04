const socket = io(); 
const ModalWindow = document.getElementById('modal-window');
const OpenImage = document.getElementById('open-img');
const TimerText = document.getElementById('timer');
const Username = document.querySelector(".username").textContent;
const QuizId = ReturnLastElement(window.location.href.split("/"))
const TimerModalWindow = document.getElementById('timer-modal-window');
const BeforeTimerText = document.getElementById("modal-timer");
const TestPassing = document.getElementsByClassName('test_passing')[0];
const StudentsCount = document.getElementById("students-count").textContent.split(" ")[1];
const StudentssContainer = document.getElementById('students-container');
const BeforeDiv = document.getElementsByClassName('before-test')[0];


function ReturnLastElement(array){
    return array[array.length - 1]
};

socket.emit('createQuiz', {
    user: `${Username}`,
    quiz: `${QuizId}`
});


document.querySelector(".small-img").onclick = function () {
    ModalWindow.style.display = "flex";
    OpenImage.src = this.src;
};


ModalWindow.onclick = function (position) {
    if (position.target === ModalWindow) ModalWindow.style.display = "none";
};

let sec = 30;

function timer(){
    if(sec > 9){
        TimerText.textContent = `0:${sec--}`;
    } else{
        TimerText.textContent = `0:0${sec--}`;
    };
    if(sec < 0 ){
        clearInterval(TimerCount);
    };
};

const TimerCount = setInterval(timer, 1000);


function studentsAppear(count){
    for(let i=0; i < count; i++){
        let student = document.createElement("div");
        student.className = 'student';
        student.id = `student_${i}`

        let StudentsName = document.createElement('span');
        StudentsName.textContent = `Name`;
        StudentsName.style = 'margin-top: 1.3vh;';

        student.appendChild(StudentsName);
        StudentssContainer.appendChild(student);
    }
}

studentsAppear(parseInt(StudentsCount));
