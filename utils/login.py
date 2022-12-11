from utils.option import OrderProduct

class Login:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw

    def check(self):
        if self.user == open("username").read() and self.passw == open("password").read():
            print("\n+-----------------------------------+")
            print("|    Account Successfully Login!    |")
            print("+-----------------------------------+\n")
            while True:
                print("+-----------------------------+")
                print("|    [1] Display Product      |")
                print("|    [2] View Order           |")
                print("|    [3] Exit                 |")
                print("+-----------------------------+")
                print("\n")
                try:
                    print("--------------------------------------")
                    option = int(input("    Select an option: "))
                    print("--------------------------------------")
                    print("\n")
                    order_class = OrderProduct()
                except ValueError:
                    print("Numbers Only Please")
                else:
                    if option == 1:
                        order_class.display_column()
                        order_class.display_order()
                    elif option == 2:
                        order_class.viewOrder()
                    elif option == 3:
                        exit()
                    else:
                        print("+-------------------------------------+")
                        print("|           Invalid Input             |")
                        print("+-------------------------------------+")
                        print("")
                        order_class.display_order()
        else:
            print("\n+-------------------------------------+")
            print("|   Incorrect username or password    |")
            print("+-------------------------------------+")
