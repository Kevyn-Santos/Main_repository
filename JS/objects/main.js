let firstName = "Maria";
let tela = this;


class People{//modelo para se contruir objetos
    nome;
    idade;
    trabalho;
    anoNascimento
    constructor(nome, idade, trabalho){//São "valores padrão" para essa classe, mas no caso eu digo que tais valores padrao devem ser declarados se nao eles ficam indefinidos.
        this.nome = nome;// this se refere a propriedade do objeto aonde ele esta, então "o nome do objeto people se refere a nome do construtor"
        this.idade = idade;
        this.trabalho = trabalho;
        this.anoNascimento = 2023 - idade;
    }
    descrever(){
        console.log(`ola, eu sou ${this.nome}, tenho ${this.idade} anos de idade, e trabalho como ${this.trabalho}`);
        // aqui eu digo que sera pego o nome, idade, e trabalho do objeto onde a função esta dentro. Se o this não fosse usado a função usaria as variaveis globais com nome, idade e trabalho. e como nesse caso não existem variaveis globais então da um problema de variavel não declarada.
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
console.log(Person.greetings());