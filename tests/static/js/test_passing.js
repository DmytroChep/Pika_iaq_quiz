const ModalWindow = document.getElementById('modal-window');
const OpenImage = document.getElementById('open-img');
const TimerText = document.getElementById('timer');

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