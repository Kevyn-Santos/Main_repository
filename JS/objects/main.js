
class People{//modelo para se contruir objetos
    nome;
    idade;
    trabalho;
    anoNascimento
    constructor(nome, idade, trabalho){//São "valores padrão" para essa classe, mas no caso eu digo que tais valores padrao devem ser declarados se nao eles ficam indefinidos.
        this.nome = nome;
        this.idade = idade;
        this.trabalho = trabalho;
        this.anoNascimento = 2023 - idade;
    }
    descrever(){
        console.log(`ola, eu sou ${this.nome}, tenho ${this.idade} anos de idade, e trabalho como ${this.trabalho}`);
    };
}

let Person = {//object literal, um objeto ja instanciado sem a necessidade de uma classe
    firstName: "John",
    lastName: "Titor",
    date: 2006,
    greetings: function(){
        console.log(`Olá, meu nome é ${this.firstName}`);
    }
};
function person(first, last, year){
    this.firstName = first;
    this.lastName = last;
    this.year = year;
};

let carinha = new People("John", 50, "engenheiro");// instancia, objeto construido a apartir do modelo "People"
/* carinha.nome = "john";
carinha.idade = 50;
carinha.trabalho = "engenheiro";
instancias nao são declaradas desse jeito, mas sim entre os parenteses da variavel 'carinha' */
console.log(descrever());