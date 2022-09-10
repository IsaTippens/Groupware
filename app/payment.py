from app.screen.titled_screen import TitledScreen
from app.Test import Test
#from app.movies import MovieScreen

from app.globals import BookingService, MovieService, State, TheatreService

def snacks_cost(item: str):
    """
    This function will take a string as a parameter and assign a cost to the item. 
    We will iterate over the snacks list, to get the cost
    """
    if (item == "Popcorn"):
        return 25
    elif (item == "Candy"):
        return 25
    elif (item == "Slushie"):
        return 25
    else:
        return 0

def calc_cost(snack_list : list):
    """
    uses the snacks_cost function to iterate over the list
    """
    total_cost = 0
    for snack in snack_list:
        total_cost = total_cost + snacks_cost(snack)
    return total_cost



class Payment(TitledScreen):
    def __init__(self):
        super().__init__("Payment")

    def start(self):
        super().start()
        Ticket = State["TICKET"]
        #get ticket details
        print("Your Ticket details are as follows: ")
        print(f"Movie: {Ticket.movie.name}")
        print(f"Time: {Ticket.time}")
        print(f"Date: {Ticket.date}")
        price = len(Ticket.seats) * MovieService.get_price(Ticket.movie)
        snacks_total = calc_cost(Ticket.snacks)
        total = price+calc_cost(Ticket.snacks)
        print(f"Price for the tickets: R{price}")
        print(f"Price for the snacks: R{snacks_total}")
        print()
        print(f"This brings your total to: R{total}")


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
                
                print(f"Thank You, {name},  for your payment of R{total} which has been charged to the card {new_card_num}")
                print("The payment has been successful. Hope you enjoy your movie :)")

                # 'registers the ticket'
                TheatreService.register_ticket(Ticket)  # expects the parameter
                BookingService.register_ticket(Ticket)


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
                    print(f"Thank You, {name} for your payment of R{total} which has been charged to the card associated to account  {account_num}")
                    print("The payment has been successful. Hope you enjoy your movie :)")
                      # 'registers the ticket'
                    TheatreService.register_ticket(Ticket)  # expects the parameter
                    BookingService.register_ticket(Ticket)
                else:
                    print("The bank you selected does not exist. Payment Failed. Try again. ")
                    
            else:
                return self.goBack()
            return self.navigateToRoot()
        else:
            pass #placeholder for now
            print("You selected an option that does not allow us to proceed with the payment. ")
            confirmation = input("Enter '0', if you wish to no longer proceed with the payment, which will end this process. ")
            if (confirmation == '0'):
                pass # end process
                return self.navigateToRoot()
            else:
                return self.navigate(Payment())  # start from over
