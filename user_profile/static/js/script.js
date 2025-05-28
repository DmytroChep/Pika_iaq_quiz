const filter_all = document.getElementById("all")
const filter_recently = document.getElementById("recently")
const filter_madeByYou = document.getElementById("madeByYou")
const filter_favourite = document.getElementById("favourite")



filter_all.addEventListener("click", () => {
    filter_all.style.backgroundColor = "#F5D23B"
    filter_recently.style.backgroundColor = "white"
    filter_madeByYou.style.backgroundColor = "white"
    filter_favourite.style.backgroundColor = "white"
})

filter_recently.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    filter_recently.style.backgroundColor = "#F5D23B"
    filter_madeByYou.style.backgroundColor = "white"
    filter_favourite.style.backgroundColor = "white"
})

filter_madeByYou.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    filter_recently.style.backgroundColor = "white"
    filter_madeByYou.style.backgroundColor = "#F5D23B"
    filter_favourite.style.backgroundColor = "white"
})

filter_favourite.addEventListener("click", () => {
    filter_all.style.backgroundColor = "white"
    filter_recently.style.backgroundColor = "white"
    filter_madeByYou.style.backgroundColor = "white"
    filter_favourite.style.backgroundColor = "#F5D23B"
})