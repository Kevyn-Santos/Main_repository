const numbers =[1,2,3,4,5];
const Doubled = numbers.map(double);

console.log(numbers); 
/* console.log(Doubled); */


function double(element, index, array){
   return array[index] = element * 2;
}
