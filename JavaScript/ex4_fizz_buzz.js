// 4. Replace numbers divisible by 3 with a word "Fizz", numbers divisible by 5 with a word "Buzz" and numbers divisible by 3 and 5 with a word "FizzBuzz"

function fizz_buzz(){
    for (let i = 1; i <= 101; i++){
        if (i % 3 === 0 && i % 5 === 0){
            console.log("FizzBuzz")
        }
        else if (i % 3 === 0){
            console.log("Fizz")
        }
        else if (i % 5 === 0){
            console.log("Buzz")
        }
        console.log(i)
    }
}

fizz_buzz();