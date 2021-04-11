class Budget:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.expenditure = 0

    def deposit(self):
        amount = int(input("Enter the amount you want to deposit: \n"))
        print("You have deposited {} to {}".format(amount, self.name))


    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: \n"))

        if self.balance >= amount:
            if amount >= 200:
                self.balance -= amount
                self.expenditure += amount
            else:
                print("You can't take less than N200")
                exit()
        else:
            print("Insufficient Funds")

    def getBalance(self):
        print("{} have N{}".format(self.name, self.balance))
        return self.balance


    def Transfer(self):
        transfer = int(input("Enter the amount you want to transfer: \n"))
        trans = input("Enter the category you want to transfer to: \n")
        print("You have transfer {} sucessfully to {}".format(transfer, trans))
        

class Food(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__( name )


class Clothing(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__( name )

class Entertainment(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__( name )

class Rent(Budget):
    def __init__(self):
        name = type(self).__name__
        super().__init__( name )

food = Food()
food.deposit()
print(food.deposit)

