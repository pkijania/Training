// 3. Create menu with list exercises - Sort numbers, find min and max value, count the amount of even and odd numbers, reverse values, check if a word or a number is a palindrome

const prompt = require ("prompt-sync")();

class Validators{
    digit(prompt_text, error){
        let input_digit = prompt(prompt_text);
        while (Number.isInteger(+input_digit) !== true){
            input_digit = prompt(error);
        }
        return parseInt(input_digit, 10);
    }

    new_list(){
        const validators = new Validators();
        let list = [];
        let which_list = "0";
        while (which_list != "default" || which_list != "custom"){
            which_list = String(prompt("Use default list (1, 2, 0, 2, 1) or custom list? (default/custom): "));
            if (which_list === "default"){
                list = [1, 2, 0, 2, 1];
                break;
            }
            else if (which_list === "custom"){
                let list_length = validators.digit("How many digits?: ", "Wrong digit, please type a correct digit: ");
                for (let i = 0; i < list_length; i++){
                    let number = validators.digit("Type a digit: ", "Wrong digit, please type a correct digit: ");
                    list.push(number);
                }
                break;
            }
            else{
                console.log("Wrong input. Input should be (default) or (custom)")
            }
        }
        return list;
    }
}

class List_exercises{
    sort(list){
        let end = false;
        for (let i = 1; i <= list.length; i++){
            for (let j = 0; j <= list.length - 1; j++){
                if (list[j] > list[j + 1]){
                    let temp = list[j]
                    list[j] = list[j + 1] 
                    list[j + 1] = temp
                    end = true;
                }
            }
            if (end === false){
                break;
            }
        }
        return list;
    }

    min_max(list){
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
        return [min, max];
    }

    even(list){
        let even_number = 0;
        let odd_number = 0;
        for (let i of list){
            if (i % 2 === 0){
                even_number += 1;
            }
            else if (i % 2 != 0){
                odd_number += 1;
            }
        }
        return [even_number, odd_number];
    }

    reverse(list){
        let new_list = [];
        while (list.length){
            new_list.push(list.pop());
        }
        return new_list;
    }

    palindrome(list){
        for (let i = 0; i < list.length/2; i++){
            if (list[i] != list[list.length - 1 - i]){
                return false;
            }
        }
        return true;
    }
}

if (require.main === module){
    const validators = new Validators();
    const list_exercises = new List_exercises();
    let list = validators.new_list();
    let menu_first = "\nWhat would you like to do?: ";
    let menu_second = "Wrong action, choose again: ";
    let menu_third = "Your list is:";
    while (true){
        console.log("\nMenu");
        console.log("1 = Show info about a list");
        console.log("2 = Modify a list");
        console.log("3 = Exit\n");
        console.log(menu_third, list);
        let choice = validators.digit(menu_first, menu_second);
        switch (choice){
            case (1):
                while (true){
                    console.log("\nMenu:")
                    console.log("1 = Print max and min value from a list")
                    console.log("2 = Print number of even and odd digits from a list")
                    console.log("3 = Check if a list is a palindrome")
                    console.log("4 = Go back\n")
                    console.log(menu_third, list)
                    choice_info = validators.digit(menu_first, menu_second);
                    switch (choice_info){
                        case (1):
                            console.log("\nMin and max values are:", list_exercises.min_max(list))
                            break;
                        case (2):
                            console.log("\nNumber of even and odd values is:", list_exercises.even(list))
                            break;
                        case (3):
                            if (list_exercises.palindrome(list)){
                                console.log("\nIt is a palindrome")
                            }
                            else{
                                console.log("\nIt is not a palindrome")
                            }
                        case (4):
                            break;
                        default:
                            console.log("Wrong action");
                            break;
                    }
                    break;
                }
                break;
            case (2):
                while (true){
                    console.log("\nMenu:")
                    console.log("1 = Create a new list")
                    console.log("2 = Sort a list")
                    console.log("3 = Reverse a list")
                    console.log("4 = Go back\n")
                    console.log(menu_third, list)
                    let choice_modify = validators.digit(menu_first, menu_second);
                    switch (choice_modify){
                        case (1):
                            list = validators.new_list();
                            break;
                        case (2):
                            list = list_exercises.sort(list);
                            break;
                        case (3):
                            list = list_exercises.reverse(list);
                            break;
                        case (4):
                            break;
                        default:
                            console.log("Wrong action");
                            break;   
                    }
                    break;
                }
                break;
            case (3):
                return list;
            default:
                console.log("Wrong action");
                break;                    
        }
    }
}