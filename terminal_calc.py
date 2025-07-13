from ast import main
import math
def add():  #defining the function wich multiplies the two values chosen by he user
    value_1 = float(input("Enter first Number: "))
    value_2 = float(input("Enter second Number: "))
    summ = (value_1 + value_2)
    print(f"your summ for your addition is {summ}")


def subtract(): #is the function to subtracts the two values
    value_1 = float(input("Enter first Number: "))
    value_2 = float(input("Enter second Number: "))
    summ = (value_1 - value_2)
    print(f"your summ for your subtraction is {summ}")

    
def multiply():# multiplys the given values
    value_1 = float(input("Enter first number of the multiplication: "))
    value_2 = float(input("Enter second number of the multiplication: "))
    summ = (value_1 * value_2)
    print(f" your summ of your multiplication is {summ}")



def divide():
    value_1 = float(input("Enter the first number for the division: "))
    value_2 = float(input("enter the second number for your division: "))
    summ = (value_1 /value_2)
    print(f"your summ of your division is {summ}")


while True: #this is a loop to make a menu from where the user can choose from wich function he wants to use for wich calc.
        print("select a method to calculate")
        print("1.Add")
        print("2.subtract")
        print("3.multiply")
        print("4.divide")
        print("5.exit")
        choice = int(input("enter your choice: "))
        if choice == 1:
            add()
        elif choice == 2:
            subtract()
        elif choice == 3:
            multiply()
        elif choice == 4:
            divide()
        elif choice == 5:
            print("exiting the calc app, see you again bye from ilvi:)")
            break
        else:
            print("invalid choice, please ry it again or report it to me if its a bug")
if __name__ == "__main__":
   main()