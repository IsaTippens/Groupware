from ast import Tuple
from app.screen.titled_screen import TitledScreen
from app.globals import State, MovieService, TheatreService, BookingService
from core.viewmodels import Ticket
from core.utils import TheatreUtils
from datetime import date


class TheatreSummary(TitledScreen):
    def __init__(self):
        super().__init__("Theatre", "Summary")

    def get_tickets_for_movie(self, tickets, movie, movie_date):
        result = []
        for ticket in tickets:
            if ticket.movie.name == movie.name and ticket.date == movie_date:
                result.append(ticket)
        return result

    def print_seats(self, seats):
        vacant = len(seats) * len(seats[0])
        nonvacant = 0
        for i in range(len(seats)):
            result = (TheatreUtils.index_to_letter(i)+"\t")         
            row = seats[i] 
            for j in range(len(row)):
                print("\t",j+1,end='')
                col = row[j]
                if col == True:
                    result += "|*|\t"
                    nonvacant += 1
                else:
                    result += "| |\t"
            print("\n"+result + "\n") 
        print("-" * 5)
        print(f"Available seats: {vacant - nonvacant}")
        print(f"Occupied seats: {nonvacant}")
        print(f"Total seats: {vacant}")
        print("-" * 5)
        return
    
    def get_input(self, options: list):
        while True:
            try:
                user_input = int(input("Select your choice (0 to go exit):  "))
                if user_input >= 0 and user_input <= len(options):
                    return user_input
            except:
                pass 
            print("Invalid input. Please try again")

    def start(self):
        super().start()
        dt = str(date.today())
        while True:
            print(f"Theatres for {dt}\n")
            movies = MovieService.get_all()
            selected_movie = ""
            for idx, movie in enumerate(movies):
                print(f"{idx+1}: {movie.name}")
            user_input = self.get_input(movies)
            if user_input == 0:
                break
            selected_movie = movies[user_input-1]

            times = ["2PM", "5PM", "8PM"]
            print("Available times:")
            for idx, time in enumerate(times):
                print(f"{idx+1}: {time}")
            user_input = self.get_input(times)
            if user_input == 0:
                break
            selected_time = times[user_input-1]
            theatre = TheatreService.get(selected_movie, selected_time, dt)
            print(f"Showing {selected_movie.name} at {selected_time} on {dt}")
            self.print_seats(theatre.seats)
            user_input = input("Would you like to view another theatre? (Enter \"Yes\" to continue): ")
            if user_input.lower() != "yes":
                break

                
        return self.goBack()

