class car{// não é necessario declarar as variaveis a serem usadas nos metodos, elas ja serao declaradas nas classes filhas

    motorTipo(){
        console.log(`o motor é do tipo ${this.motor}`);
    }
    rodasTipo(){
        console.log(`as rodas são ${this.rodas}`);
    }
    portasTipo(){
        console.log(`As portas são ${this.portas}`);
    }
    
}
class f1 extends car{//aqui eu digo que a classe f1 é uma extensão da classe car, portanto essa deve ter as mesmas caracteristicas daquela.
    motor = "v6";
    rodas = "aro13";
    portas = "sem portas";
}
class Range extends car{
    motor = "v8";
    rodas = "aro18";
    portas ="quadruplas";
}

const formula1 = new f1(); //é necessario criar um objeto para acessar os metodos das classes, então nao usar o static keyword. provavelmente tem uma forma sim de acessar diretamente das classes e eu so nao descobri ainda.
const Ranger = new Range();
console.log(Ranger.rodasTipo());
console.log(Ranger.motorTipo());
console.log(Ranger.portasTipo());