const regex = /[^A-Z]/g;

const alvo1 = "ABC123";
const alvo2 = "XYZ";
const alvo3 = "abc";

console.log(alvo1.match(regex)); //["1","2","3"]
console.log(alvo2.match(regex)); //null
console.log(alvo3.match(regex)); //["a","b","c"]

//Validação de entrada de usuário:
//const regex = /[^A-Za-z0-9]/;

//Limpeza de Strings:
//const input = "Oi, Estudante!";
//cconst cleaned = input.replace(/[^A-Za-z0-9]/g, "");
//console.log(cleaned); // Isso resultará em "OiEstudante"