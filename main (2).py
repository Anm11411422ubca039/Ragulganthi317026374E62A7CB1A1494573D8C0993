[01/11, 12:28 pm] +91 6374 882 520: class player:
    def play (self):
        print("The player is playing cricket.")
class Batsman(player):
    def play(self):
        print("The batsman is bating.")
class Bowler (player):
    def play(self):
        print("The bowler is bowling.")
        
batsman=Batsman()  
bowler=Bowler() 

batsman.play()
bowler.play()
[01/11, 12:28 pm] +91 6374 882 520: class Account:
    def __init__(self):
        self.balance=0
        print('Your Account is Created.')
    def deposit(self):
        amount=int(input('Enter the amount to deposit:'))
        self.balance+=amount
        print('Your New Balance =%d' %self.balance)
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw:'))
        if(amount>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance-=amount
        print('Your Remaining Balance =%d' %self.balance)
    def enquiry(self):
        print('Your Balance =%d' %self.balance)

account= Account()
account.deposit()
account.withdraw()
account.enquiry()