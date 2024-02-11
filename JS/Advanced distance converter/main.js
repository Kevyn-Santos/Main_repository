let convertType = "miles";
const heading = document.querySelector('h1');
const intro = document.querySelector('p');
const answerDiv = document.querySelector('answer');
const form = document.querySelector('convert');

document.addEventListener("keydown", function(event){
    let key = event.code;
    console.log(key);
   
    if(key === "KeyK"){

        convertType = "kilometers";
        heading.innerHTML = `Kilometers to Miles Converter`;
        intro.innerHTML = `Type in a number of kilometers and click the button to convert the distance to miles.`;

    }else if(key === "KeyM"){

        convertType = "miles";
        heading.innerHTML = `Miles to Kilometers Converter`;
        intro.innerHTML = `Type in a number of miles and click the button to convert the distance to kilometers.`;
    
    }

    console.log(convertType);

});


document.getElementById("convert").addEventListener("submit", function(event){
    event.preventDefault();
    const distance = parseFloat(document.getElementById("distance").value);
    const answer = document.getElementById("answer");

    
   
    if(distance){
        if(convertType == "miles"){
            
            let result = (distance * 1.609).toFixed(3); //arruma um numero para ate x casas decimais, mas transforma ele numa string
            answer.innerHTML = `<h2> ${distance} miles converts to ${result} quilometers </h2>`;
        
            console.log (answer);

        }else if (convertType == "kilometers"){
            let result = (distance / 1.609).toFixed(3); //arruma um numero para ate x casas decimais, mas transforma ele numa string
            answer.innerHTML = `<h2> ${distance} kilometers converts to ${result} miles </h2>`;
        
            console.log (answer);

        }
    }else{
        answer.innerHTML = ("You didn't put a number");
    };

});

