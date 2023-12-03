// 5. Find min and max value

function min_max(){
    let list = [80, 21, 2, 0, 100, 5, 8, 25, 64];
    let max = list[0];
    let min = list[0];
    for (let i of list){
        if (i < min){
            min = i;
        }
        if (i > max){
            max = i;
        }
    }
    console.log(min, "min")
    console.log(max, "max")       
}

min_max();