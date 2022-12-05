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
            
