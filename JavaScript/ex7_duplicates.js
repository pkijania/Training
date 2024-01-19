// 7. Create a list with random numbers and delete duplicates

const prompt = require ("prompt-sync")();

class Duplicates{
    counstructor(){
        console.log("This program creates a list and then deletes all duplicates")
    }

    create_list(){
        this.old_list = [];
        this.list_length = parseInt(prompt("How many digits? "), 10);
        for (let i = 0; i < this.list_length; i++){
            this.old_list.push(Math.floor(Math.random() * this.list_length));
        }
    }

    create_set(){
        this.temp_set = new Set();

        for (let item of this.old_list){
            this.temp_set.add(item);
        }
    }

    convert_to_list(){
        this.new_list = Array.from(this.temp_set);
    }

    show_outcome(){
        if (this.old_list.length === this.new_list.length){
            console.log("List without duplicates:", this.new_list)
        }
        else{
            console.log("List:", this.old_list, "List without duplicates:", this.new_list)
        }
    }
}

if (require.main === module){
    try {
        let duplicates = new Duplicates();
        duplicates.create_list();
        duplicates.create_set();
        duplicates.convert_to_list();
        console.log(duplicates.show_outcome())
    }
    catch (error) {
        console.error(error)
    }
}