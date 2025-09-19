let PlusButton = document.querySelector('#plus')
const Additional = document.getElementsByClassName("additional")[0];
const QuestionsNumbers = document.getElementsByClassName("questions-numbers")[0];
let questCount = 1;
let QuestionsAll = [];
let form = document.getElementById('quiz_1');
let currentQuest = 1;
const quest_text= document.getElementById("question_text");
const answers_text= document.getElementsByClassName('answer');
const cor_answers = document.getElementsByClassName('correct_answer');
const formDom = document.querySelector("#quiz_1")
const modalQuizName = document.querySelector(".modalBg")
const modalQuizName2 = document.querySelector(".modalBg2")
const QuizNameBtn = document.querySelector(".buttonSubmit")
const QuizNameInput = document.querySelector(".quizName")

QuizNameBtn.addEventListener("click", () => {
    if (QuizNameInput.value != ""){
        modalQuizName.style.display = "none"
        modalQuizName2.style.display = "none"
    }
})



document.querySelector(".returnToMain").addEventListener("click", () => {
    let countQuestion = 1;
    const allQuestions = document.querySelectorAll(".content");
    
    const formData = new FormData();
    
    formData.append('quiz_name', QuizNameInput.value);
    
    const fileInput = document.querySelector(".quizImage");
    if (fileInput.files && fileInput.files.length > 0) {
        formData.append('quiz_avatar', fileInput.files[0]);
    }
    
    const questions = {};
    
    allQuestions.forEach(element => {
        let stringyfiedCount = `${countQuestion}`;
        questions[stringyfiedCount] = {
            questionTitle: document.querySelector(`.content${stringyfiedCount} .main-content .question #question_text`).value,
            answer1: {
                title: document.querySelector(`.content${stringyfiedCount} .main-content .necessary #answer1 #answer_input`).value
            },
            answer2: {
                title: document.querySelector(`.content${stringyfiedCount} .main-content .necessary #answer2 #answer_input`).value
            },
            answer3: {},
            answer4: {}
        };
        
        const additionalAnswers = document.querySelectorAll(`.content${stringyfiedCount} .main-content .additional .answer`);
        if (additionalAnswers.length !== 0) {
            const answer3Input = document.querySelector(`.content${stringyfiedCount} .main-content .additional #answer3 #answer_input`);
            const answer4Input = document.querySelector(`.content${stringyfiedCount} .main-content .additional #answer4 #answer_input`);
            
            if (answer3Input) questions[stringyfiedCount].answer3.title = answer3Input.value;
            if (answer4Input) questions[stringyfiedCount].answer4.title = answer4Input.value;
        }
        
        countQuestion++;
    });
    
    formData.append('questions', JSON.stringify(questions));
    
    $.ajax({
        url: '/save_test',
        type: 'POST',
        data: formData,
        processData: false, 
        contentType: false, 
        success: function(response) {
            location.href = "/";
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
});

function getLocalCount(){
    let count = document.querySelectorAll(`.content${questCount} .main-content .additional .answer`).length + 2
    return count
}

function ChooseQuestion(){
    document.querySelectorAll(".quest-number").forEach((element) => {
        element.addEventListener("click", () => {
            document.querySelector(`.content${questCount}`).style.display = "none"
            questCount = element.textContent
            document.querySelector(`.content${questCount}`).style.display = "flex"
        })
    })
}

function addImageForInputsFunc(){
    const questionImageInput = document.querySelectorAll(".addImageInputQuestion")
    questionImageInput.forEach((element) => {
        element.addEventListener("change", function(event){
            let answerCount = element.id[element.id.length - 1] 
            const ImageCheck = document.querySelector(`.content${questCount} .main-content .question #answerImageQuestion`)
            console.log(ImageCheck)
            const selectedFiles = event.target.files;
            const urlImageObj = URL.createObjectURL(selectedFiles[0])
    
            if (!ImageCheck){          
                let imageDom = document.createElement("img")
                imageDom.src = urlImageObj
                imageDom.classList.add("questionImg")
                imageDom.id = `answerImageQuestion`
                document.querySelector(`.content${questCount} .main-content .question`).appendChild(imageDom)
            } else{
                ImageCheck.src = urlImageObj
            }
        }) 
    })
    let addImageInputs = document.querySelectorAll(`.content${questCount} .main-content .necessary .answer .addImageInput`)
    let addImageInputsAdditional = document.querySelectorAll(`.content${questCount} .main-content .additional .answer .addImageInput`)
    // document.querySelectorAll(`.content${questCount} .main-content .additional .answer .addImageInput`).forEach((element) => {
    //     console.log(element)
    //     addImageInputs.push(element)
    // })
    addImageInputs.forEach((element) => {
        element.addEventListener("change", function(event){
            let answerCount = element.id[element.id.length - 1]
            console.log(answerCount) 
            const ImageCheck = document.querySelector(`.content${questCount} .necessary .answer #answerImage${answerCount}`) 
            const selectedFiles = event.target.files;
            const urlImageObj = URL.createObjectURL(selectedFiles[0])
    
            if (!ImageCheck){          
                let imageDom = document.createElement("img")
                imageDom.src = urlImageObj
                imageDom.classList.add("AnswerImage")
                imageDom.id = `answerImage${answerCount}`
                document.querySelector(`.content${questCount} .necessary #answer${answerCount} `).appendChild(imageDom)
            } else{
                ImageCheck.src = urlImageObj
            }
        })
    })

    addImageInputsAdditional.forEach((element) => {
        element.addEventListener("change", function(event){
            let answerCount = element.id[element.id.length - 1]
            console.log(answerCount) 
            const ImageCheck = document.querySelector(`.content${questCount} .additional .answer #answerImage${answerCount}`) 
            const selectedFiles = event.target.files;
            const urlImageObj = URL.createObjectURL(selectedFiles[0])
    
            if (!ImageCheck){          
                let imageDom = document.createElement("img")
                imageDom.src = urlImageObj
                imageDom.classList.add("AnswerImage")
                imageDom.id = `answerImage${answerCount}`
                document.querySelector(`.content${questCount} .additional #answer${answerCount}`).appendChild(imageDom)
            } else{
                ImageCheck.src = urlImageObj
            }
        })
    })
}

addImageForInputsFunc()




function addAnswer(){
    let count = getLocalCount()
    count ++
    let Additional = document.querySelector(`.content${questCount} .main-content .additional`)
    let newAnswer = document.createElement('div')
    let PlusButton = document.querySelector(`.content${questCount} .main-content .additional #plus`)
    newAnswer.className = "answer";
    newAnswer.id = `answer${String(count)}`;
    PlusButton.style = 'width: 39.7vw;';

    let input = document.createElement('input');
    input.type = 'checkbox';
    input.value = count;
    input.name = 'correct_answer[]';
    input.id = 'checkbox';

    let inputTypeFile = document.createElement("input")
    inputTypeFile.type = "file"
    inputTypeFile.className = "addImageInput"
    inputTypeFile.id = `inputImage${count}`

    let answerInput = document.createElement('input');
    answerInput.type = "text";
    answerInput.placeholder = "Enter an answer";
    answerInput.name = 'answer[]';
    answerInput.id = "answer_input"
        
    let addButton = document.createElement('label');
    addButton.setAttribute("for", `inputImage${count}`)
    addButton.className = 'addImageBtn';
    let image = document.createElement('img');
    image.src = '/tests/static/images/add_image.svg';
    image.className = "addImageLogo"
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
    newAnswer.appendChild(inputTypeFile)
    newAnswer.appendChild(addButton);
    newAnswer.appendChild(answerInput);
    Additional.appendChild(newAnswer);
    
    PlusButton.remove()
    Additional.appendChild(PlusButton)
    
    addImageForInputsFunc()

    
    if (count == 4){
        PlusButton.remove()
    }
}

function deleteAnswer(id){
    // count--;
    let count = getLocalCount()
    count --
    let Additional = document.querySelector(`.content${questCount} .main-content .additional`)
    let answer = document.getElementById(id);
    let PlusButton = document.querySelector(`.content${questCount} .main-content .additional #plus`)
    answer.remove();
    if (count == 3){
        let PlusButton = document.createElement('div');
        PlusButton.id = 'plus';
        PlusButton.type = 'button';
        PlusButton.style = 'width: 39.7vw;'
        // document.querySelectorAll("#plus").forEach((element) => {
        //     element.addEventListener("click", addAnswer)
        // })
        // PlusButton.onclick = () => addAnswer();
        let span = document.createElement("span");
        span.textContent = "+";
        PlusButton.appendChild(span)
        
        Additional.appendChild(PlusButton)
        document.querySelectorAll("#plus").forEach((element) => {
            element.addEventListener("click", addAnswer)
        })
    }
    if (count == 2){
      PlusButton.style = "width: 79.7vw;"  
    }    
    }

function addQuestion(){
    if (questCount <20 ){

        questCount++;
        let quest = document.createElement('button');
        quest.className = 'quest-number';
        quest.id = questCount;
        quest.textContent = questCount;
        // quest.onclick = () => changeQuest(quest.id);
        currentQuest = quest.id;
        QuestionsNumbers.appendChild(quest);


        const contentDiv = document.createElement('div');
        contentDiv.classList.add("content", `content${questCount}`)
        

        const mainContent = document.createElement('div');
        mainContent.className = 'main-content';
        contentDiv.appendChild(mainContent)
        
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';
        
        const addImageInputQuestion = document.createElement('input');
        addImageInputQuestion.type = 'file';
        addImageInputQuestion.className = 'addImageInputQuestion';
        addImageInputQuestion.id = 'inputImageQuestion';
        
        const addImageLabelQuestion = document.createElement('label');
        addImageLabelQuestion.htmlFor = 'inputImageQuestion';
        addImageLabelQuestion.className = 'addImageBtnQuestion';
        
        const addImageLogoQuestion = document.createElement('img');
        addImageLogoQuestion.src = '/tests/static/images/add_image.svg';
        addImageLogoQuestion.alt = '■';
        addImageLogoQuestion.className = 'addImageLogo';
        
        addImageLabelQuestion.appendChild(addImageLogoQuestion);
        
        const questionInput = document.createElement('input');
        questionInput.type = 'text';
        questionInput.placeholder = 'Enter text of a question';
        questionInput.name = 'question_text';
        questionInput.id = 'question_text';
        
        const questionNumber = document.createElement('span');
        questionNumber.id = 'number-quest';
        questionNumber.textContent = `question ${questCount}`;
        
        questionDiv.appendChild(addImageInputQuestion);
        questionDiv.appendChild(addImageLabelQuestion);
        questionDiv.appendChild(questionInput);
        questionDiv.appendChild(questionNumber);
        
        const necessaryDiv = document.createElement('div');
        necessaryDiv.className = 'necessary';
        
        const answer1 = document.createElement('div');
        answer1.className = 'answer';
        answer1.id = 'answer1';
        
        const checkbox1 = document.createElement('input');
        checkbox1.type = 'checkbox';
        checkbox1.id = "checkbox"
        checkbox1.value = '1';
        checkbox1.name = 'correct_answer[]';
        checkbox1.className = 'correct_answer';
        
        const fileInput1 = document.createElement('input');
        fileInput1.type = 'file';
        fileInput1.className = 'addImageInput';
        fileInput1.id = 'inputImage1';
        
        const fileLabel1 = document.createElement('label');
        fileLabel1.htmlFor = 'inputImage1';
        fileLabel1.className = 'addImageBtn';
        
        const fileLogo1 = document.createElement('img');
        fileLogo1.src = '/tests/static/images/add_image.svg';
        fileLogo1.alt = '■';
        fileLogo1.className = 'addImageLogo';
        
        fileLabel1.appendChild(fileLogo1);
        
        const answerInput1 = document.createElement('input');
        answerInput1.type = 'text';
        answerInput1.placeholder = 'Enter an answer';
        answerInput1.name = 'answer[]';
        answerInput1.id = "answer_input"
        
        answer1.appendChild(checkbox1);
        answer1.appendChild(fileInput1);
        answer1.appendChild(fileLabel1);
        answer1.appendChild(answerInput1);
        
        const answer2 = document.createElement('div');
        answer2.className = 'answer';
        answer2.id = 'answer2';
        
        const fileInput2 = document.createElement('input');
        fileInput2.type = 'file';
        fileInput2.className = 'addImageInput';
        fileInput2.id = 'inputImage2';
        
        const checkbox2 = document.createElement('input');
        checkbox2.type = 'checkbox';
        checkbox2.value = '2';
        checkbox2.id = "checkbox"
        checkbox2.name = 'correct_answer[]';
        checkbox2.className = 'correct_answer';
        
        const fileLabel2 = document.createElement('label');
        fileLabel2.htmlFor = 'inputImage2';
        fileLabel2.className = 'addImageBtn';
        
        const fileLogo2 = document.createElement('img');
        fileLogo2.src = '/tests/static/images/add_image.svg';
        fileLogo2.alt = '■';
        fileLogo2.className = 'addImageLogo';
        
        fileLabel2.appendChild(fileLogo2);
        
        const answerInput2 = document.createElement('input');
        answerInput2.type = 'text';
        answerInput2.placeholder = 'Enter an answer';
        answerInput2.name = 'answer[]';
        answerInput2.id = "answer_input"
        
        answer2.appendChild(fileInput2);
        answer2.appendChild(checkbox2);
        answer2.appendChild(fileLabel2);
        answer2.appendChild(answerInput2);
        
        necessaryDiv.appendChild(answer1);
        necessaryDiv.appendChild(answer2);
        
        const additionalDiv = document.createElement('div');
        additionalDiv.className = 'additional';
        
        const plusButton = document.createElement('button');
        plusButton.id = 'plus';
        plusButton.type = 'button';
        
        const plusSpan = document.createElement('span');
        plusSpan.textContent = '+';
        
        plusButton.appendChild(plusSpan);
        additionalDiv.appendChild(plusButton);
        
        const fileInput = document.createElement('input');
        fileInput.type = 'file';
        fileInput.accept = 'image/*';
        fileInput.id = 'file';
        fileInput.style.display = 'none';
        
        mainContent.appendChild(questionDiv);
        mainContent.appendChild(necessaryDiv);
        mainContent.appendChild(additionalDiv);
        
        formDom.appendChild(contentDiv);

        document.querySelector(`.content${questCount -1}`).style.display = "none"
        ChooseQuestion()
        document.querySelectorAll("#plus").forEach((element) => {
            element.addEventListener("click", addAnswer)
        })
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
    
