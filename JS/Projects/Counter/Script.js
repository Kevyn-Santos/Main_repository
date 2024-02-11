const number = document.querySelector("#number");
const decrease = document.querySelector(".decrease-btn");
const reset = document.querySelector(".reset-btn");
const increase = document.querySelector(".increase-btn");
let counter = 0;

increase.addEventListener("click", function(){
    counter++;
    number.innerHTML = counter;
    console.log(counter);
});

decrease.addEventListener("click", function(){
    counter--;
    number.innerHTML = counter;
    console.log(counter);
});

reset.addEventListener("click", function(){
    counter = 0;
    number.innerHTML = counter;
    console.log(counter);
});