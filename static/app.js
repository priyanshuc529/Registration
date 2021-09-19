const video = document.querySelector(".video-container");
const close = document.getElementById("close");
const normal = document.querySelector(".normal")
const volume = document.querySelector(".group")

window.addEventListener("DOMContentLoaded",function(){
    video.play()
    video.defaultPlaybackRate = 4.0;
})

volume.addEventListener("click",function(){
    volume.classList.remove('fa-volume-off');
    volume.classList.remove("group");
    video.muted = false;
})

close.addEventListener('click',function(){
    normal.classList.add('disable');
    volume.classList.remove('fa-volume-off');
    video.muted = false;
})


