import math

#----------------------------------- English ----------------------------------------------------#

author = "belain3d"
version = "1.0"

class english:
    
    def calc_eng():

        def twonumber(num1, num2):
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            return num1, num2

        def menu():
            print("add",    "       Sum"  )
            print("subt",   "      Subtract"   )
            print("mult",   "      Multiply"   )
            print("div",    "       Divide"  )
            print("mod",    "       Modulo"  )
            print("exp",    "       Exponentiate"  )
            print("exit"    "       Exit")
            print("")

        print("Calculator program by", author)
        print("Version:", version)
        print("Type 'list' for more commands.")
        enter = input(": ")
        while enter != 'exit':
            if enter == 'list':
                menu()
            elif enter == 'add':
                try:
                    num1 = int(input("Type your first number: "))
                    num2 = int(input("Type your second number:  "))
                    print("The sum is:", num1+num2)
                except ValueError:
                    print("Invalid input!")
            elif enter == 'subt':
                try:
                    num1 = int(input("Type your first number: "))
                    num2 = int(input("Type your second number:  "))
                    print("The subtraction is:", num1-num2)
                except ValueError:
                    print("Invalid input!")
            elif enter == 'mult':
                try:  
                    num1 = int(input("Type your first number: "))
                    num2 = int(input("Type your second number:  "))
                    print("The multiplication is:", num1*num2)
                except ValueError:
                    print("Invalid input!")
            elif enter == 'div':
                try:
                    num1 = int(input("Type your first number: "))
                    num2 = int(input("Type your second number:  "))
                    print("The division is:", num1/num2)
                except ZeroDivisionError:
                    print("You can't divide with zero!")
                except ValueError:
                    print("Invalid input!")
            elif enter == 'mod':
                num1 = int(input("Type your first number: "))
                num2 = int(input("Type your second number:  "))
                print("The modulo is:", num1%num2)
            elif enter == "exp":
                num1 = int(input("Type your first number: "))
                num2 = int(input("Type your second number:  "))
                print("The exponentiation is:", num1**num2)
            else:
                print("Invalid command, please try again.")
            enter = input(": ")
        if enter == "exit":
            print("Thank you for using belain3d's program. Cheers!")
