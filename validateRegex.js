const validate = require("safe-regex");

const regex = process.argv[2];

const result = validate(regex) ? "safe" : "not safe";

console.log(`Regex Pattern /${regex}/ is ${result}.`);
