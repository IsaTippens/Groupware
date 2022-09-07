from app.screen.titled_screen import TitledScreen
from app.Test import Test
from app.movies import MovieScreen

from app.globals import State

class Payment(TitledScreen):
    def __init__(self):
        super().__init__("Payment")

    def start(self):
        super().start()
        print("The state is: ", State.get("test", "Empty"))
        print()
        print("Select payment type: ")
        print("1\t Visa")
        print("2\t Mastercard")
        print("3\t Instant EFT")
        print()

        num = input("Enter your payment type as indicated above using the corresponding number: ")
        if (num == "1") or (num =="2") :  # if Visa or Mastercard
            card_num = input("Enter your card number: ")
            card_holder = input("Enter the card holder's name: ")
            card_exp = input("Enter the card expiration date in the MM/YY format: ")
            card_cvv = input("Enter the CVV number: ")

            """use card number and replace most of the numbers with an '*'
            we will show the first 4 and last 4 digits
            """
            new_card_num = card_num[0:4]  + " **** **** " +  card_num[-4:]
            
            # part with the values ? ...
            print()
            print("The payment has been successful. Thank You. ")

        elif num == "3": # instant EFT
            print("Select bank from the list below: ")
            print("1\t Standard Bank")
            print("2\t Capitec")
            print("3\t ABSA")
            print("4\t FNB")
            print("5\t Nedbank")

            # part with the values? ...
            bank_list = ["1","2","3","4","5"]
            bank = input("Enter the bank according to the numbers in the above list: ")
            if bank in bank_list:
                account_num = input("Enter the account number: ")
                passcode = input("Enter the passcode: ")
                print("Attempting to log in...")
                print()
                print("Log in successful ! ")
                print()
                print("Please open your banking app or internet banking to authorise the payment")
                print()
                print("The payment has been successful ")
            else:
                print("The bank you selected does not exist. Payment Failed. Try again")
                #super().start()   
                

        
        else:
            return self.goBack()
        return self.navigate(Test())
