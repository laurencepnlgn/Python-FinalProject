from utils.option import OrderProduct

class Display():
    def display_mainscreen():
        while True:
            print("+-----------------------------+")
            print("|    [1] Display Product      |")
            print("|    [2] View Order           |")
            print("|    [3] Exit                 |")
            print("+-----------------------------+")
            print("\n")
            print("--------------------------------------")
            Display.display_option(int(input("    Select an option: ")))
            print("--------------------------------------")
            print("\n")

    def display_option(option):
        if option == 1:
            x = OrderProduct()
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

