document.getElementById("convert").addEventListener("submit", function(event){
    event.preventDefault();
    const distance = parseFloat(document.getElementById("distance").value);
    const answer = document.getElementById("answer");
   
    if(distance){

        let result = (distance * 1.609).toFixed(3); //arruma um numero para ate x casas decimais, mas transforma ele numa string
        answer.innerHTML = `<h2> ${distance} miles converts to ${result} quilometers </h2>`;
    
        console.log (answer);
    }else{alert("You didn't put a number");}

});