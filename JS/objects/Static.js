class person {
    static name = "john";
    static age = 500;
    static hello(){
        console.log(`Hello, i'm ${this.name}, and i am ${this.age} years old`)
    }
}

console.log(person.hello());//aqui ao inves de criar um objeto para acessar certas propriedades eu consigo acessar diretamente as propriedades com static.