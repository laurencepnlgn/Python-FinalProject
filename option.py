class OrderProduct():
    def __init__(self, data = []):
        self.data = data
        self.dp1 = ["|   0601","|    RAM","     |      2,000      |"]
        self.dp2 = ["|   0602","|    CPU","     |      9,000      |"]
        self.dp3 = ["|   0603","|    MOBO","    |      7,499      |"]
        self.dp4 = ["|   0604","|    CASE","    |      1,399      |"]
        self.dp5 = ["|   0605","|    RGB FAN"," |      120        |"]
        self.dp6 = ["|   0606","|    SSD","     |      950        |"]
        self.dp7 = ["|   0607","|    HDD","     |      800        |"]
        self.dp8 = ["|   0608","|    MONITOR"," |      5,500      |"]
        self.dp9 = ["|   0609","|    KEYBOARD","|      1,199      |"]
        self.dp10= ["|   0610","|    MOUSE","   |      499        |"]
        self.dp11= ["|   0611","|    HEADSET"," |      8,99       |"]
        self.dp12= ["|   0612","|    PSU","     |      2,995      |"]
        self.dp13= ["|   0613","|    GPU","     |      19,200     |"]
        self.dp14= ["+----------------+---------------------+-----------------+"]
        self.dplay = [self.dp1, self.dp2, self.dp3, self.dp4, self.dp5, self.dp6, self.dp7, 
                    self.dp8, self.dp9, self.dp10, self.dp11, self.dp12, self.dp13, self.dp14]
        
    def display(self):
        print("+----------------+---------------------+-----------------+")
        print("|----------------|---------------------|-----------------|")
        print("|   ProductID    |    ProductName      |      Price      |")
        print("|----------------|---------------------|-----------------|")
        print("+----------------+---------------------+-----------------+")
        for i in self.dplay: #DISPLAYING PRODUCT
            print("         ".join(i))
    
    def order_product(self, product):
        print("\n")
        print("+----------------+---------------------+-----------------+")
        print("|----------------|---------------------|-----------------|")
        print("|   ProductID    |    ProductName      |      Price      |")
        print("|----------------|---------------------|-----------------|")
        print("+----------------+---------------------+-----------------+")
        
        if product == "0601" or product == "RAM":
            item = "RAM"
            print("         ".join(self.dp1))
            print("\n")
            
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 2000
            
            print("\n")
            confirmation = input("Confirm Order [y] | [n]: ")
            if confirmation == "y" or confirmation == "Y":
                print("\n")
                print(" ------------------------------------")
                print(" |  Computer Parts Ordering System  |")
                print(" |       Rizal Ave. Bats City       |")
                print(" |      www.computerpartsos.com     |")
                print(" |     Welcome to Computer Parts    |")
                print(" |          Ordering System         |")
                print(" ------------------------------------")
                print("     Customer Name: ", customer_name)
                print(" ------------------------------------")
                print("     Item: RAM")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
                
        elif product == "0602" or product == "CPU":
            item = "CPU"
            print("         ".join(self.dp2))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 9000
            
            print("\n")
            confirmation = input("Confirm Order [y] | [n]: ")
            if confirmation == "y" or confirmation == "Y":
                print("\n")
                print(" ------------------------------------")
                print(" |  Computer Parts Ordering System  |")
                print(" |       Rizal Ave. Bats City       |")
                print(" |      www.computerpartsos.com     |")
                print(" |     Welcome to Computer Parts    |")
                print(" |          Ordering System         |")
                print(" ------------------------------------")
                print("     Customer Name: ", customer_name)
                print(" ------------------------------------")
                print("     Item: Central Processing Unit (CPU)")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
