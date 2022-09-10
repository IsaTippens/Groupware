from app.screen.titled_screen import TitledScreen
from app.Test import Test
#from app.movies import MovieScreen

from app.globals import BookingService, State, TheatreService
from core.viewmodels import ticket
from core.viewmodels.ticket import Ticket

class Payment(TitledScreen):
    def __init__(self):
        super().__init__("Payment")

    def start(self):
        super().start()
        #get ticket details , use booking service
        print("Your Ticket details are as follows: ")
        print("Movie: " + Ticket.movie.name)
        print("Time: " + Ticket.time)
        print("Date: " + Ticket.date)
        price = len(Ticket.seats) * (ticket.movie.type)
        print("Price: " )


        # get confirmation to proceed with the payment
        response =  input("Enter 'Y' if you would like to proceed with the ticket(s) payment with the details above: ")
        if (response == "Y") or (response == "y"):
            name =  input("Kindly enter your name: ")
            State["TICKET"].owner = name


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
                
                print()
                print("The payment has been successful. Thank You. ")

                # 'registers the ticket'
                TheatreService.register_ticket(ticket)  # expects the parameter
                BookingService.register_ticket(ticket)


                #navigate to home page
                return self.navigateToRoot()

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
                      # 'registers the ticket'
                    TheatreService.register_ticket(ticket)  # expects the parameter
                    BookingService.register_ticket(ticket)
                else:
                    print("The bank you selected does not exist. Payment Failed. Try again. ")
                
                    

            
            else:
                return self.goBack()
            return self.navigate(Test())
        else:
            pass #placeholder for now
            print("You selected an option that does not allow us to proceed with the payment. ")
            confirmation = input("Enter '0', if you wish to no longer proceed with the payment, which will end this process. ")
            if (confirmation == '0'):
                pass # end process
                return self.navigateToRoot()
            else:
                return self.navigate(Payment())  # start from over
