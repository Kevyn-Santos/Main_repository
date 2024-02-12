class veiculo{
    constructor(Modelo, motor, tamanho){
        this.modelo = Modelo;
        this.motor = motor;
        this.tamanho = tamanho;
    }
}

class carro extends veiculo{
    constructor(Modelo,motor,tamanho, aro){
        super(Modelo, motor, tamanho);
        this.aro = aro;
    }
}

class avião extends veiculo{
    constructor(Modelo, motor, tamanho, armamento){
        super(Modelo, motor, tamanho);
        this.armamento = armamento;
    }
}

class navio extends veiculo{
    constructor(Modelo, motor, tamanho, peso){
        super(Modelo, motor, tamanho);
        this.peso = peso;
    }
}

let range = new carro("Range rover", "V8", "3 metros", 18);
let FW = new avião("Focke Wulf", "V8", "7.3 metros", "MG131" );
let Titanic = new navio("Olympic-class", "2 motores de tripla expansão", "269 metros", "46.328 toneladas");

console.log(range);
console.log(FW);
console.log(Titanic);