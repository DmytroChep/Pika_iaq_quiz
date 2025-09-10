let PlusButton = document.querySelector('#plus')
const Additional = document.getElementsByClassName("additional")[0];
const QuestionsNumbers = document.getElementsByClassName("questions-numbers")[0];
let count = 2;
let questCount = 1;
let QuestionsAll = [];
let form = document.getElementById('quiz_1');
let currentQuest = 1;
const quest_text= document.getElementById("question_text");
const answers_text= document.getElementsByClassName('answer');
const cor_answers = document.getElementsByClassName('correct_answer');

const addImageInputs = document.querySelectorAll(".addImageInput")
const questionImageInput = document.querySelector(".addImageInputQuestion")

addImageInputs.forEach((element) => {
    element.addEventListener("change", function(event){
        let answerCount = element.id[element.id.length - 1] 
        const ImageCheck = document.querySelector(`#answerImage${answerCount}`)
        const selectedFiles = event.target.files;
        const urlImageObj = URL.createObjectURL(selectedFiles[0])

        if (!ImageCheck){          
            let imageDom = document.createElement("img")
            imageDom.src = urlImageObj
            imageDom.classList.add("AnswerImage")
            imageDom.id = `answerImage${answerCount}`
            document.querySelector(`#answer${answerCount}`).appendChild(imageDom)
        } else{
            ImageCheck.src = urlImageObj
        }
    })
})
questionImageInput.addEventListener("change", function(event){
        let answerCount = questionImageInput.id[questionImageInput.id.length - 1] 
        const ImageCheck = document.querySelector(`#answerImage${answerCount}`)
        const selectedFiles = event.target.files;
        const urlImageObj = URL.createObjectURL(selectedFiles[0])

        if (!ImageCheck){          
            let imageDom = document.createElement("img")
            imageDom.src = urlImageObj
            imageDom.classList.add("questionImg")
            imageDom.id = `answerImageQuestion`
            document.querySelector(`.question`).appendChild(imageDom)
        } else{
            ImageCheck.src = urlImageObj
        }
    })


function addAnswer(){
    Additional.innerHTML += `<div class="answer" id="answer${count}">
    <input type="checkbox" value="${count}" name = "correct_answer[]" id="checkbox" class="correct_answer">
    <input type="file" class="addImageInput" id="inputImage${count}">
                        <label for="inputImage${count}" class = "addImageBtn"><img src="/tests/static/images/add_image.svg" alt="■" class = "addImageLogo"></label>
                        <input type="text" placeholder="Enter an answer" id="answer_input" name="answer[]">
                    </div>`
        console.log(count)
        count++;
    if (count == 4){
        PlusButton.style.display = "none"
        alert(PlusButton)
    }
    
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
