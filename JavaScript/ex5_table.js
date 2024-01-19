// 5. Create and display a table of n columns and n rows and count the sum of all it's elements

const prompt = require ("prompt-sync")();

class Table{
    constructor(){
        this.list = [];
        this.sum = 0;
    }

    type_data(){
        this.row = parseInt(prompt("How many rows? "), 10);
        this.column = parseInt(prompt("How many columns? "), 10);
    }

    create_table(){
        this.digit = 0;
        for (let i = 0; i < this.row; i++){
            this.list[i] = [];
            this.digit = parseInt(prompt("Type a digit: "), 10);
            for (let j = 0; j < this.column; j++){
                this.list[i][j] = this.digit + "";
            }
        }
    }

    sum_of_elements(){
        for (let i = 0; i < this.row; i++){
            for (let j = 0; j < this.column; j++){
                this.sum += parseInt(this.list[i][j], 10);
            }
        }
        console.log(this.list, "\nSum of elements in a table is: " + this.sum)
    }
}

if (require.main === module){
    try {
        let table = new Table();
        table.type_data();
        table.create_table();
        table.sum_of_elements();
    }
    catch (error) {
        console.error(error)
    }
}