from ast import Tuple
from app.screen.titled_screen import TitledScreen
from app.globals import State, MovieService, TheatreService, BookingService
from core.viewmodels import Ticket
from core.utils import TheatreUtils


class TicketManagementScreen(TitledScreen):
    def __init__(self):
        super().__init__("Ticket", "Management")
        self.options = [self.change_owner, self.change_time]
        self.option_names = ["Change owner", "Select new time"]

    def fetch_ticket(self) -> Tuple(Ticket, bool):
        ticket = None
        while True:
                t_id = input("Enter ticket id (Enter 0 to exit): ")
                if not t_id.isdigit():
                    print("Enter a valid ticket id")
                    continue
                t_id = int(t_id)
                if t_id == 0:
                    return ticket, True
                ticket = BookingService.get(t_id)
                if ticket.id != t_id:
                    print("Ticket #", t_id, " does not exist")
                    continue
                break
        return ticket, False

    def deregister_ticket(self, ticket):
        TheatreService.deregister_ticket(ticket)

    def register_ticket(self, ticket):
        TheatreService.register_ticket(ticket)
        BookingService.update(ticket)

    def change_owner(self, ticket):
        while True:
            name = input("Enter your name (Enter \"exit\" to cancel): ")
            confirm = input(f"Are you sure you want to change {ticket.owner} to {name}? (Enter \"yes\" to confirm): ")
            if confirm != "yes":
                continue
            self.deregister_ticket(ticket)
            ticket.owner = name
            self.register_ticket(ticket)
            print("Ticket Successfully registered")
            return
        pass

    def check_if_seats_available(self, ticket: Ticket, date: str, time: str) -> bool:
        theatreB = TheatreService.get(ticket.movie, date, time)
        seats = theatreB.seats
        for seat in ticket.seats:
            row, col = TheatreUtils.split_seat(seat)
            r_int = TheatreUtils.letter_to_index(row)
            c_int = col - 1
            if seats[r_int][c_int] == True:
                return False
        return True

    def change_time(self, ticket: Ticket):
        times = ["2PM", "5PM", "8PM"]
        print("Available times")
        for idx, time in enumerate(times):
            print(idx + 1, time)

        while True:
            user_choice = input("Select a time (Enter \"exit\" to cancel): ")
            if user_choice == "exit":
                return

            if not user_choice.isdigit():
                print("Enter a valid number")
                continue

            user_choice = int(user_choice)
            if user_choice > len(times) or user_choice <= 0:
                print("Enter a valid option")
                continue
            time = times[user_choice - 1]
            if time == ticket.time:
                print("Select a different time than displayed on the ticket")
                continue
            
            if not self.check_if_seats_available(ticket, ticket.date, time):
                print("Seats displayed on the ticket are unavailable for the time selected")
                continue
            
            confirm = input(f"Are you sure you want to change from {ticket.time} to {time} (Enter \"yes\" to confirm): ")
            if confirm == "yes":
                break
            
        time = times[user_choice - 1]
        self.deregister_ticket(ticket)
        ticket.time = time
        self.register_ticket(ticket)

    def start(self):
        super().start()
        ticket, exit = self.fetch_ticket()
        
        if exit:
            return self.goBack()
        while True:
            print("Ticket details:", ticket)
            print("Select an option")
            for idx, option in enumerate(self.option_names):
                print(f"{idx + 1}: {option}")
            user_choice = 0
            while True:
                user_choice = input("Enter a number (Enter 0 to exit): ")
                if user_choice == "exit":
                        return

                if not user_choice.isdigit():
                    print("Enter a valid number")
                    continue

                user_choice = int(user_choice)
                if user_choice > len(self.options) or user_choice < 0:
                    print("Enter a valid option")
                    continue
                break
            if user_choice == 0:
                break
            self.options[user_choice-1](ticket)
                
        return self.goBack()

