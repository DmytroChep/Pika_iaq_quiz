const backTomain = document.querySelector(".main_icon")
const save_avatar = document.querySelector(".button")
const logoutBtn = document.querySelector(".logoutBtn")


backTomain.addEventListener("click", () => {
    window.location.href = "/"
})

save_avatar.addEventListener("change", function(event){
    const selectedFiles = event.target.files;
    document.querySelectorAll(".user_avatar")[1].src = URL.createObjectURL(selectedFiles[0])   
})
