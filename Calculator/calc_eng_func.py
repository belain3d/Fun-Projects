class english:

    def calc_eng():

        def help():
            print("add")
            print("subtract")
            print("multiply")
            print("divide")
            print("modulus")
            print("square")
            print("cube")
            print("exponentiate")
            print("help")
            print("exit")

        def add(num1, num2):
            return num1+num2

        def subtract(num1, num2):
            return num1-num2
        
        def multiply(num1, num2):
            return num1*num2
        
        def divide(num1, num2):
            return num1/num2

        def modulus(num1, num2):
            return num1%num2
        
        def square(num):
            return num*num
        
        def cube(num):
            return num*num*num

        def exponentiate(num1, num2):
            return num1**num2

        print("Welcome to belain3d's calculator program!")
        print("Please input \"help\" below if you don't know the commands\n")
        enter = input(": ")
        
        while True:

            if enter == "help":
                help()

            elif enter == "add":
                try:
                    num1 = int(input("Input the first number: "))
                    num2 = int(input("Input the second number: "))
                    print(add(num1, num2))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "subtract":
                try:
                    num1 = int(input("Input the first number: "))
                    num2 = int(input("Input the second number: "))
                    print(subtract(num1, num2))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "multiply":
                try:
                    num1 = int(input("Input the first number: "))
                    num2 = int(input("Input the second number: "))
                    print(multiply(num1, num2))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "divide":
                try:
                    num1 = int(input("Input the first number: "))
                    num2 = int(input("Input the second number: "))
                    print(divide(num1, num2))
                except ValueError:
                    print("Please input number instead.")
                except ZeroDivisionError:
                    print("You can't divide with zero!")

            elif enter == "modulus":
                try:
                    num1 = int(input("Input the first number: "))
                    num2 = int(input("Input the second number: "))
                    print(modulus(num1, num2))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "square":
                try:
                    num = int(input("Input the number: "))
                    print(square(num))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "cube":
                try:
                    num = int(input("Input the number: "))
                    print(cube(num))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "exponentiate":
                try:
                    num1 = int(input("Input the first number: "))
                    num2 = int(input("Input the second number: "))
                    print(exponentiate(num1, num2))
                except ValueError:
                    print("Please input number instead.")

            elif enter == "exit":
                    print("\nThank you for trying out my program!")
                    break

            enter = input(": ")
