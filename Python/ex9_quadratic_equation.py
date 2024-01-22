# 9. Solve the 'ax^2 + bx + c = 0' quadratic equation and test it.

import math

class QuadraticEquation:
    def __init__(self):
        self.a = self.delta = self.x0 = self.x1 = self.x2 = 0
        self.x = "no solutions"

    def type_data(self):
        while self.a == 0:
            self.a = float(input("Type first digit (a): "))
            if self.a == 0:
                print("(a) can't be 0, please type another digit: ")
        self.b = float(input("Type second digit (b): "))
        self.c = float(input("Type third digit (c): "))
    
    def count(self):
        self.delta = self.b**2 - 4 * self.a * self.c
        if self.delta > 0:
            self.x1 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
            self.x2 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
            return self.x1, self.x2
        elif self.delta == 0:
            self.x0 = -self.b / (2 * self.a)
            return self.x0
        else:
            return self.x

    def test(self):
        self.a = 1
        self.b = 2
        self.c = 1
        self.outcome = self.count()
        assert self.outcome == -1.0, "Assertion failed, outcome should be -1.0"

if __name__ == "__main__":
    try:
        print("Program solves the 'ax^2 + bx + c = 0' quadratic equation.")
        choice = int(input("1. Launch a program, \n2. Launch test, \nYour choice: "))
        equation = QuadraticEquation()
        if choice == 1:
            equation.type_data()
            print("Outcome:", equation.count())
        elif choice == 2:
            equation.test()
        else:
            print("Wrong choice.")
    except Exception as error:
        print(f"Error!!, program shut down due to {error}")