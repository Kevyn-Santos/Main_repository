let numbers = [1,2,3,4,5];

numbers.forEach(Double);//para cada elemento do array numeros, execute a função double, isso é um exemplo de Callback;
numbers.forEach(Display);// depois mostre o resultado de cada elemento, isso tambem;

function Double(element, index, array){//a ordem dos parametros de alguma fora altera oresultado
    array[index] = element * 2;
};

function Display(element){
    console.log(element);
};

