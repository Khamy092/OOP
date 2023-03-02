# Challenge 2:

""" 
Create a class called "BankAccount" that has attributes for the account holder's name and balance. 
Write methods to deposit and withdraw money from the account, and to calculate
the interest earned on the balance. 

"""

class BankAccount():
    
    def __init__(self, holder_name, account_balance):

        self.holder_name = holder_name
        self.account_balance = account_balance

    def widthraw(self, widthraw_amount):

        """
        This function take the account_balance and subtracts the widthrawal amount
        and returns the remaining amount.
        """
        self.account_balance -= widthraw_amount

        return self.account_balance - widthraw_amount

    def deposit(self, deposit_amount):

        """
        This function take the account_balance and adds the deposit amount
        and returns the sum.
        """
        self.account_balance += deposit_amount

        return self.account_balance + deposit_amount
    
    def calculate_interest(self, interest_rate):

        """
        This function takes the account_balance and use the basic formula to calculate interest
        earned on the account_balance in 1 year.
        """
        return self.account_balance * interest_rate
    


Customer_1212 = BankAccount("John Smith", 150000) # instance of an object.

print("Main Balance: " + str(Customer_1212.account_balance))

Customer_1212.deposit(25000) # deposting money
print("Deposting 25,000")
print("New Balance: " + str(Customer_1212.account_balance))

Customer_1212.widthraw(10000) # widthrawing money
print("Widthrawing 10,000")
print("Balance after Widthrawing: " + str(Customer_1212.account_balance))

interest_earned = Customer_1212.calculate_interest(0.025) # interst earned in a year with %2.5 rate
print("Interest earned in a year: " + str(interest_earned))

Customer_1212.deposit(interest_earned) # deposting the interest earned
print("Total balance with interest: " + str(Customer_1212.account_balance))