let PlusButton = document.getElementById('plus');
const Additional = document.getElementsByClassName("additional")[0];
const QuestionsNumbers = document.getElementsByClassName("questions-numbers")[0];
let count = 3;
let questCount = 1;
let QuestionsAll = [];
let form = document.getElementById('quiz_1');
let currentQuest = 1;
const quest_text= document.getElementById("question_text");
const answers_text= document.getElementsByClassName('answer');
const cor_answers = document.getElementsByClassName('correct_answer');



function addAnswer(){
    if (count == 4){
        PlusButton.remove()
    }
        let newAnswer = document.createElement('div')
        newAnswer.className = "answer";
        newAnswer.id = `answer${String(count)}`;


        let input = document.createElement('input');
        input.type = 'checkbox';
        input.value = count;
        input.name = 'correct_answer[]';
        input.id = 'checkbox';
        
        let answerInput = document.createElement('input');
        answerInput.type = "text";
        answerInput.placeholder = "Enter an answer";
        answerInput.name = 'answer[]';
        
        let addButton = document.createElement('button');
        addButton.type = 'button';
        addButton.id = 'addit_button';
        addButton.onclick = () => document.getElementById('file').click();
        let image = document.createElement('img');
        image.src = '/tests/static/images/add_image.svg';
        addButton.appendChild(image)
        addButton.id = 'deleteButton';
        
        let deleteButton = document.createElement("button");
        deleteButton.type = 'button';
        deleteButton.onclick = ()=> deleteAnswer(newAnswer.id);
        let delImage = document.createElement('img');
        delImage.src = "/tests/static/images/bin.svg";
        delImage.id = 'delImage';
        deleteButton.appendChild(delImage);
        
        let top = document.createElement("div");
        top.id = 'top';
        top.appendChild(input);
        top.appendChild(deleteButton);

        newAnswer.appendChild(top);
        newAnswer.appendChild(addButton);
        newAnswer.appendChild(answerInput);
        
        count++;
        Additional.appendChild(newAnswer);
}

function deleteAnswer(id){
    count--;
    let answer = document.getElementById(id);
    answer.remove();
    if (count == 4){
        PlusButton = document.createElement('div');
        PlusButton.id = 'plus';
        PlusButton.type = 'button';
        PlusButton.onclick = () => addAnswer()
        let span = document.createElement("span");
        span.textContent = "+";
        PlusButton.appendChild(span)
        Additional.appendChild(PlusButton)
    }
}

function addQuestion(){
    if (questCount <50 ){

        questCount++;
        let quest = document.createElement('button');
        quest.className = 'quest-number';
        quest.id = questCount;
        quest.textContent = questCount;
        quest.onclick = () => changeQuest(quest.id);
        currentQuest = quest.id;
        QuestionsNumbers.appendChild(quest);
    }

}

// document.getElementById('save').addEventListener(
//     type= 'click',
//     listener =  function(event) {
//         event.preventDefault()
            
//         let formData = new FormData(form);

//         let quiz = {
//             question: formData.get("question_text"),
//             answers: formData.getAll("answer[]"),
//             correct: formData.getAll("correct_answer[]")
//         };

//         QuestionsAll.push(quiz);
//         console.log(QuestionsAll);
//     }
// );
    

// function changeQuest(num) {
//     currentQuest = num;
//     let button = document.getElementsByClassName('quest-number')[num - 1];
//     let text = document.getElementById('number-quest');
//     text.textContent = `question ${button.textContent}`;}
//     if (QuestionsAll.length > num - 1){
//         q = QuestionsAll[num - 1];
//         console.log(q);
//         quest_text.textContent = q.question;
//         for (let a = 0; a < answers_text.length; a++) {
//         answers_text[a].textContent = q.answers[a];
//         }
//     };
