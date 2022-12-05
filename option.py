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
        elif product == "0603" or product == "MOTHERBOARD":
            item = "MOTHERBOARD"
            print("         ".join(self.dp3))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 7499
            
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
                print("     Item: MOTHERBOARD")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
                
        elif product == "0604" or product == "CASE":
            item = "CASE"
            print("         ".join(self.dp4))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 1399
            
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
                print("     Item: CASE")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
        
        elif product == "0605" or product == "RGB FAN":
            item = "RGB FAN"
            print("         ".join(self.dp5))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 120
            
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
                print("     Item: RGB FAN")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
                    
        elif product == "0606" or product == "SSD":
            item = "SSD"
            print("         ".join(self.dp6))
            print("\n")
    
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 950
            
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
                print("     Item: SOLID STATE DRIVE (SSD)")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
        
        elif product == "0607" or product == "HDD":
            item = "HDD"
            print("         ".join(self.dp7))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 800
            
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
                print("     Item: HARD DISK DRIVE (HDD)")
                print("     Amount: ", amount)  
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)
                          
        elif product == "0608" or product == "MONITOR":
            item = "MONITOR"
            print("         ".join(self.dp8))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 5500
            
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
                print("     Item: MONITOR")
                print("     Amount: ", amount)  
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)

        elif product == "0609" or product == "KEYBOARD":
            item = "KEYBOARD"
            print("         ".join(self.dp9))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 1199
            
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
                print("     Item: KEYBOARD")
                print("     Amount: ", amount)  
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list) 
                
        elif product == "0610" or product == "MOUSE":
            item = "MOUSE"
            print("         ".join(self.dp10))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 499
            
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
                print("     Item: MOUSE")
                print("     Amount: ", amount)  
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)               

        elif product == "0611" or product == "HEADSET":
            item = "HEADSET"
            print("         ".join(self.dp11))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 899
            
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
                print("     Item: HEADSET")
                print("     Amount: ", amount)  
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list) 
               
        elif product == "0612" or product == "PSU":
            item = "PSU"
            print("         ".join(self.dp12))
            print("\n")
        
            customer_name = str(input("Enter Customer Name: "))
            amount = int(input("Order Amount: "))
            total = amount * 2995
            
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
                print("     Item: POWER SUPPLY (PSU)")
                print("     Amount: ", amount)
                print(" ------------------------------------")
                print("     Total Price: ", total)
                print(" ------------------------------------")
                customer_list = " ".join(["Customer Name:", customer_name, "Item:",item, "Amount:", str(amount), "Total Price:", str(total)])
                self.data.append(customer_list)          
