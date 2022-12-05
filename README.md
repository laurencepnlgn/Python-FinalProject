# Python-FinalProject - COMPUTER PARTS ORDERING SYSTEM

## Login
      1. Create a class for login - Login()
            1. Constructor accept two parameters
             username and password
            2. Inside the constructor, create an attribute and set a default value for each instance
             Example: self.user = "admin or ADMIN"
             Example: self.passw = "admin123 or ADMIN123"
      2. Create a method for login - we use if else statement

## Order Product
      1. Create a class for order product - OrderProduct()
            1. Inside the constructor, we create an attribute for each PC Part
                  Example: self.dp1 = ["0601", "RAM", "2000"] 
      2. Create a method for ordering system - def order_product()
            1. Method should accept one parameter - def order_product(self, product)
            2. Create a user input - Order Product: 
                  1. Print the ordered product
            3. Create a user input - Order Amount: 
            4. Create a user input for order confirmation - Confirm Order [y] | [n]: 
                  1. If "y", print the receipt
                  2. Elif "n", go back to the main screen

## Main Screen
      1. Create welcome screen
      2. Display option and ask the user
         Example: Select an option
            [1] Order Product
            [2] View Order
            [3] Exit 
          1. If == 1 display Order Product
          2. Elif == 2 display View Order
          3. EIif == 3 then Exit else print Invalid Input!

## Developer
      1. Panaligan, John Laurence 
      2. Besa, Ella Mae
      3. Serrano, Laica 

## Subject and Section
      CS 121 - Advanced Computer Programming
      IT - 2101
