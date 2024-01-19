// 8. Create a list with random numbers and count every number

const prompt = require ("prompt-sync")();

class CountNumbers{
    counstructor(){
        console.log("This program creates list and counts its numbers")
    }

    create_list(){
        this.list = [];
        this.list_length = parseInt(prompt("How many digits? "), 10);
        for (let i = 0; i < this.list_length; i++){
            this.list.push(Math.floor(Math.random() * this.list_length));
        }
    }

    show_list(){
        console.log("Your list is:", this.list)
    }
    
    create_dictionary(){
        this.dictionary = {};
        for (let i of this.list){
            this.dictionary[i] = 0;
        }
    }

    count_numbers(){
        for (let i of this.list){
            if (this.dictionary[i] === 0){
                this.dictionary[i] = 1;
            }
            else{
                this.dictionary[i] = this.dictionary[i] + 1;
            }
        }
    }

    get_outcome(){
        return this.dictionary;
    }
}

if (require.main === module){
    try {
        let count_numbers = new CountNumbers();
        count_numbers.create_list();
        count_numbers.show_list();
        count_numbers.create_dictionary();
        count_numbers.count_numbers();
        console.log("(Digit, number of digits)", count_numbers.get_outcome())
    }
    catch (error) {
        console.error(error)
    }
}