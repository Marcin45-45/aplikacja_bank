

class Bank:
    def __init__(self):
        self.amount = 0
        self.overdraft_limit = 1000

    def add_money(self, money):
        
        if money <= 0:
            raise ValueError('Kwota wpłaty musi być większa od 0, popraw wartość proszę') 
        self.amount += money
        return money

    def withdraw_money(self, money):
        
        if money <= 0:
            raise ValueError('Kwota wypłaty musi być większa od 0, popraw wartość proszę')
        
        if self.amount - money < -self.overdraft_limit:
            raise ValueError('Nie masz wystarczających środków na koncie, aby dokonać tej wypłaty. Przekracza ona limit debetu.')   
        
        self.amount -= money
        return money
           

# PIN
correct_pin = '1234'
attempts = 0
max_attempts = 3

authenticated = False

while attempts < max_attempts:
    pin = input('Please enter your pin number: ') 
    if pin == correct_pin:
        print('Correct pin number, welcome to your bank account!')
        authenticated = True
        break
    else: 
        attempts += 1
        print('Wrong PIN number, please try again')

    if not authenticated and attempts >= max_attempts:
        print('Too many incorrect attempts, your account has been locked. Please contact the bank for assistance.')
        exit()


    
   
   
# Tworzymy konto:
account = Bank()

while True:
    option = input("If you want add money press 'a', if you want withdraw press 'w', if you want quit press 'q': ")

    if option == 'a':
        try:
            addmoney = int(input("How much money do you want to add to your bank account? "))
            account.add_money(addmoney)
            print(f'Your account has now: {account.amount} zł')
        except ValueError as e:
            print(e)

    elif option == 'w':
        try:
            withdraw = int(input("How much money do you want to withdraw from your bank account? "))
            account.withdraw_money(withdraw)
            print(f'Your account has now: {account.amount} zł')
        except ValueError as e:
            print(e)
            

    elif option == 'q':
        print("Thanks for using our bank service. See you next time!")
        break