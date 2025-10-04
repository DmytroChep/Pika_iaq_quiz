const filter_all = document.getElementById("all")
const allTestsDiv = document.getElementById("allTests")
const filter_madeByYou = document.getElementById("madeByYou")
const userTestsDiv = document.getElementById("userTests")
const nameUsernameRedirect = document.querySelector(".nameUsername")
const newButtonRedirect = document.querySelector(".newButton")
const joinBtn = document.querySelector(".joinButton")
const Username = document.querySelector(".username")

const socket = io(); 


joinBtn.addEventListener("click", () => {
    const quizNumber = document.querySelector(".findText").value
    socket.emit('connectQuiz', {
    user: `${Username}`,
    quizNumber: `${quizNumber}`
    });
    window.location.href = `test_passing/${quizNumber}/`
})
nameUsernameRedirect.addEventListener("click", () => {
    location.href = "/profile"
})

newButtonRedirect.addEventListener("click", ()=> {
    window.location.href = `/test_creation/`
})


filter_all.addEventListener("click", () => {
    filter_all.style.backgroundColor = "#5AB9EA"
    allTestsDiv.style.display = "flex"
    filter_madeByYou.style.backgroundColor = "white"
    userTestsDiv.style.display = "none"
})

filter_madeByYou.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    allTestsDiv.style.display = "none"
    filter_madeByYou.style.backgroundColor = "#5AB9EA"
    userTestsDiv.style.display = "flex"
})

document.querySelectorAll(".test").forEach((element) => {
    element.addEventListener("click", () => {
        window.location.href = `/test_passing/${element.id}`
    })
})