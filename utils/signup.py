class Signup:
    @staticmethod
    def sign_up_acct():
        filename = "username";
        with open(filename, "w") as f:
            f.write(input("Enter a username: "));

        filename = "password";
        with open(filename, "w") as f:
            f.write(input("Enter a password: "));
        print("+-------------------------------------+")
        print("|    Account Created Successfully!    |")
        print("+-------------------------------------+")
        print("")
