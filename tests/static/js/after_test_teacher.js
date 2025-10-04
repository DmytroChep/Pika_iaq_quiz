const Percent = document.getElementById("percent").textContent.split(" ")[2];
const StudentsCount = document.getElementById("student-text").textContent.split(" ")[1];
const StudentssContainer = document.getElementById('students-container');

function changeScore(value){
    const bar = document.querySelector('#average-score');
    const text = document.getElementById('average-score');
    bar.style.setProperty('--percent', value);
    text.textContent = "Average score: " + value;
}
changeScore(Percent);

function studentsAppear(count){
    for(let i=0; i < count; i++){
        let student = document.createElement("div");
        student.className = 'student';
        student.id = `student_${i}`

        let div = document.createElement('div');
        div.textContent = `NameSecond name`;

        let right = document.createElement('div');
        right.id = 'right';
        let rightAnswers = document.createElement('div');
        rightAnswers.id = "right-answers";
        rightAnswers.textContent = 'Right Answers'
        let average = document.createElement('div');
        average.id = "average";
        average.textContent= 'Average %';
        right.appendChild(rightAnswers);
        right.appendChild(average);

        student.appendChild(div);
        student.appendChild(right);
        StudentssContainer.appendChild(student)
    }
}

studentsAppear(parseInt(StudentsCount));