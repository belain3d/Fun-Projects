#----------------------------------- Hungarian ----------------------------------------------------#

author = "belain3d"
version = "1.0"

class hungarian:
    def calc_hun():
        def menu():
            print("add",    "       Összeadás"  )
            print("subt",   "      Kivonás"   )
            print("mult",   "      Szorzás"   )
            print("div",    "       Osztás"  )
            print("mod",    "       Maradék"  )
            print("exp",    "       Négyzetre emelés"  )
            print("exit"    "       Kilépés")
            print("")

        print("Számológép program", author, "által")
        print("Verzió:", version)
        print("Írd be a 'list' parancsot többi parancsért.")
        enter = input(": ")
        while enter != 'exit':
            if enter == 'list':
                menu()
            elif enter == 'add':
                try:
                    num1 = int(input("Írd be az első számot: "))
                    num2 = int(input("Írd be a második számot:  "))
                    print("Az összeadás:", num1+num2)
                except ValueError:
                    print("Helytelen bevitel!!")
            elif enter == 'subt':
                try:
                    num1 = int(input("Írd be az első számot: "))
                    num2 = int(input("Írd be a második számot:  "))
                    print("A kivonás:", num1-num2)
                except ValueError:
                    print("Helytelen bevitel!!")
            elif enter == 'mult':
                try:  
                    num1 = int(input("Írd be az első számot: "))
                    num2 = int(input("Írd be a második számot:  "))
                    print("A szorzás:", num1*num2)
                except ValueError:
                    print("Helytelen bevitel!!")
            elif enter == 'div':
                try:
                    num1 = int(input("Írd be az első számot: "))
                    num2 = int(input("Írd be a második számot:  "))
                    print("Az osztás:", num1/num2)
                except ZeroDivisionError:
                    print("Nem oszthatsz nullával!")
                except ValueError:
                    print("Helytelen bevitel!!")
            elif enter == 'mod':
                num1 = int(input("Írd be az első számot: "))
                num2 = int(input("Írd be a második számot:  "))
                print("A maradék:", num1%num2)
            elif enter == "exp":
                num1 = int(input("Írd be az első számot: "))
                num2 = int(input("Írd be a második számot:  "))
                print("A négyzetre emelés eredménye:", num1**num2)
            else:
                print("Helytelen parancs, próbáld újra.")
            enter = input(": ")
        if enter == "exit":
            print("Köszönjük, hogy belain3d programját használtad. Minden jót!")