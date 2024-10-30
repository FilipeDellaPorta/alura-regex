const fs = require("fs");
const bancoCsv = "database.csv";
const banco = fs.readFileSync(bancoCsv, "utf-8");

const patternNomes = /^([A-Za-zÀ-ÿ]+)(?:\s([A-Za-zÀ-ÿ]+))+/gm;
//^([A-Za-zÀ-ÿ]+)((\s[A-Za-zÀ-ÿ]+)+) alternativa para capturas nomes intermediários

const matchNomes = banco.match(patternNomes);
console.log(`Todos os nomes:`, matchNomes);
