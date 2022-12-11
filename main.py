from utils.login import Login
from utils.signup import Signup

if __name__ == "__main__":
    while True:
        print("\n\n+--------------------------------------------------+")
        print("|                                                  |")
        print("|                   WELCOME TO                     |")
        print("|         COMPUTER PARTS ORDERING SYSTEM           |")
        print("|                    made by:                      |")
        print("|            Laurence, Ella, and Laica             |")
        print("|                                                  |")
        print("+--------------------------------------------------+\n")

        print("+-----------------------------+")
        print("|    [1] Login                |")
        print("|    [2] Sign Up              |")
        print("|    [3] Exit                 |")
        print("+-----------------------------+")
        print("\n")
        try: 
            choice = int(input("    Select an option: "))
            print("\n")
        except ValueError:
            print("Numbers Only Please.")
        else:
            if choice == 1:
                login_acc = Login(input("Enter your username: "), input("Enter your password: "))
                login_acc.check()
            elif choice == 2:
                Signup.sign_up_acct()
            elif choice == 3:
                exit()
            else:
                print("Invalid Input")
