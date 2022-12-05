from option import OrderProduct
if __name__ == "__main__":
    class Login():
        def __init__(self, user, passw):
            self.user = user
            self.passw = passw
    
        def login(self):
            if self.user == "admin" and self.passw == "admin123":
                print("\n-------------------------------")
                print('| *   Login Successfuly...  * |')
                print("-------------------------------\n")
            elif self.user == "ADMIN" and self.passw == "ADMIN123":
                print("\n-------------------------------")
                print('| *   Login Successfuly...  * |')
                print("-------------------------------\n")
            else:
                print("\n---------------------------------------------------------")
                print('| *  Invalid Username or Password. Please Try Again!  * |')
                print("---------------------------------------------------------\n")
                login_screen()
    def login_screen():
        print("------------------------------------------")
        print("|       Please login to continue...      |")
        print("------------------------------------------\n")
        acc = Login(input(' Enter Username: '), input(' Enter Password: ')) 
        acc.login()
        
    print("\n\n+-------------------------------------------------+")
    print("|                                                 |")
    print("|                   WELCOME TO                    |")
    print("|         COMPUTER PARTS ORDERING SYSTEM          |")
    print("|                    made by:                     |")
    print("|            Laurence, Ella, and Laica            |")
    print("|                                                 |")
    print("+-------------------------------------------------+\n")
    
    login_screen()
    while True:
        print("+-----------------------------+")
        print("|    [1] Display Product      |")
        print("|    [2] View Order           |")
        print("|    [3] Exit                 |")
        print("+-----------------------------+")
        print("\n")
        print("--------------------------------------")
        option = int(input("    Select an option: "))
        print("--------------------------------------")
        print("\n")
        x = OrderProduct()
        if  option == 1: 
            x.display()
            print(" ")
            x.order_product(input("Order Product:  "))
            print(" ")
        elif option == 2:
            x.viewOrder()
        elif option == 3:
            exit()
        else:
            print("+-------------------------------------+")
            print("|           Invalid Input             |")
            print("+-------------------------------------+")
            print("")    
