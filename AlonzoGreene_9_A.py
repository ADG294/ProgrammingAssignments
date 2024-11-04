class BankAcct:
    def __init__(self, name, acct_number, amount, int_rate):
        self.name = name
        self.acct_number = acct_number
        self.amount = amount
        self.int_rate = int_rate

    def deposit(self):
        amt = float(input('Enter the deposit amount: \n'))
        self.amount += amt
        print(f'You deposited: \n${amt: ,.2f}')
        print(f'Your account balance is: ${self.amount: ,.2f}')



    def withdraw(self):
        amt = float(input('Enter the withdrawal amount: \n'))
        self.amount -= amt
        print(f'You withdrew: \n${amt: ,.2f}')
        print(f'Your new account balance is: ${self.amount: ,.2f}' )


    def adjust_rate(self):
        p = self.amount
        r = self.int_rate
        t = float(input('Enter number of days: \n'))

        adj_rate = ((p * r * t) / 100) / 365
        return adj_rate


    def get_balance(self):
       print(f'Your balance is ${self.amount: ,.2f}')

    def __str__(self):
        return f'Your balance is ${self.amount: ,.2f} \nYour interest amount is ${self.adjust_rate(): ,.2f} per day'



def main():
    my_act = BankAcct('Alonzo', 103940, 3000, 7)
    print(my_act)
    my_act.deposit()
    my_act.withdraw()
    my_act.get_balance()


main()