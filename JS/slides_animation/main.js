const container = document.getElementById("content");
const previous = document.getElementById("previous");
const next = document.getElementById("next");
let currentImage = 0;
let myimage = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"];

next.addEventListener("click", function(event){
    event.preventDefault();

    currentImage++;
    if(currentImage > (myimage.length-1)){currentImage = 0};

   slide();
});

previous.addEventListener("click", function(event){
    event.preventDefault();

    currentImage--;
    if(currentImage < 0){currentImage = myimage.length-1};

    slide();
})

function slide(){
    let newSlide = document.createElement("img");
    newSlide.src = `slides/${myimage[currentImage]}`;
    newSlide.className = "fadeinimg";
    container.appendChild(newSlide);

    if(container.children.length > 2){
        container.removeChild(container.children[0]);
    };
}
