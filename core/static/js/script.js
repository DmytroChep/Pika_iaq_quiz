const filter_all = document.getElementById("all")
const filter_recently = document.getElementById("recently")
const filter_madeByYou = document.getElementById("madeByYou")
const filter_favourite = document.getElementById("favourite")
const nameUsernameRedirect = document.querySelector(".nameUsername")



nameUsernameRedirect.addEventListener("click", () => {
    location.href = "/profile"
})


filter_all.addEventListener("click", () => {
    filter_all.style.backgroundColor = "#5AB9EA"
    filter_recently.style.backgroundColor = "white"
    filter_madeByYou.style.backgroundColor = "white"
    filter_favourite.style.backgroundColor = "white"
})

filter_recently.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    filter_recently.style.backgroundColor = "#5AB9EA"
    filter_madeByYou.style.backgroundColor = "white"
    filter_favourite.style.backgroundColor = "white"
})

filter_madeByYou.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    filter_recently.style.backgroundColor = "white"
    filter_madeByYou.style.backgroundColor = "#5AB9EA"
    filter_favourite.style.backgroundColor = "white"
})

filter_favourite.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    filter_recently.style.backgroundColor = "white"
    filter_madeByYou.style.backgroundColor = "white"
    filter_favourite.style.backgroundColor = "#5AB9EA"
})