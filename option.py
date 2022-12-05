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
