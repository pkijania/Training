// 5. Find min and max value

const prompt = require ("prompt-sync")();

let list = [80, 21, 2, 0, 100, 5, 8, 25, 64];
let max = list[0];
let min = list[0];
for (i = 0; i <= list.length; i++){
    if (list[i] < min){
        min = list[i];
    }
    if (list[i] > max){
        max = list[i];
    }
}
console.log(min, "min")
console.log(max, "max")