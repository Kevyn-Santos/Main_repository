let username = "KevYn";


/* username = username.trim(); // esse metodo retira espaços
let letter = username.charAt(0);
letter= letter.toUpperCase(); 

let extrachar = username.slice(1);
extrachar = extrachar.toLowerCase();
username = letter + extrachar;
console.log(username); */
//esse codigo todo transforma a primeira letra em maiuscula e o resto em minuscula

//usando method chain

username = username.trim().charAt(0).toUpperCase() + username.trim().slice(1).toLowerCase();
console.log(username);
//esse codigo faz a mesma coisa que o de cima mas tudo em uma linha so