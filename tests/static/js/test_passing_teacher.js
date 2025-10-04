const StudentsCount = document.getElementById("students-count").textContent.split(" ")[1];
const StudentssContainer = document.getElementById('students-container');
const StartButton = document.getElementById('start');
const BeforeDiv = document.getElementsByClassName('before-test')[0];
const ModalWindow = document.getElementById('timer-modal-window');
const BeforeTimerText = document.getElementById("modal-timer");
const TestPassing = document.getElementsByClassName('test_passing')[0];
const QuestionsCount = document.getElementsByClassName('question-teacher').length
const TimerText = document.getElementById('timer');
const AddTime = document.getElementById('add-time')

function studentsAppear(count){
    for(let i=0; i < count; i++){
        let student = document.createElement("div");
        student.className = 'student';
        student.id = `student_${i}`
        
        let StudentsName = document.createElement('span');
        StudentsName.textContent = `Name`;
        StudentsName.style = 'margin-top: 1.3vh;';
        let KickButton = document.createElement('button');
        KickButton.type = 'button';
        KickButton.className = 'kick';
        KickButton.id = `kick_${i}`;
        KickButton.textContent = 'kick';
        
        student.appendChild(StudentsName);
        student.appendChild(KickButton)
        StudentssContainer.appendChild(student);
    }
}

studentsAppear(parseInt(StudentsCount));


let beforeSec = 5;

function beforeTimer(){
    BeforeTimerText.textContent = `${beforeSec--}`;
    
    if(beforeSec === -1 ){
        clearInterval(BeforeTimerCount);
        BeforeDiv.style.display= 'none';
        ModalWindow.style.display = 'none';
        TestPassing.style.display = 'flex';
        const TimerCount = setInterval(timer, 1000);
        
        let seconds = 30;
        
        function timer(){
            seconds--;
            if(seconds > 9){
                TimerText.textContent = `0:${seconds}`;
            } else{
                TimerText.textContent = `0:0${seconds}`;
            };
            if(seconds < 1 ){
                clearInterval(TimerCount);
            };
            if (seconds<15){
                AddTime.style.display='flex';
                AddTime.onclick = function () {
                    seconds+=16;
                    AddTime.remove()
                };
            }
        };

    };
};

let BeforeTimerCount;

StartButton.addEventListener('click',
    () => {
        ModalWindow.style.display = 'flex';
        BeforeTimerCount = setInterval(beforeTimer, 1000);
    }
);
