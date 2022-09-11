from app.screen.titled_screen import TitledScreen
from core.utils import TheatreUtils
from app.globals import State, TheatreService
from app.Test import Test
from core.viewmodels import Movie, Ticket
from core.enums import MovieType

class SelectSeatsScreen(TitledScreen):
    def __init__(self):
        super().__init__('SelectSeats')

    def print_seats(self, seats):
        for i in range(len(seats)):
            result = (TheatreUtils.index_to_letter(i)+"\t")         
            row = seats[i] 
            for j in range(len(row)):
                print("\t",j+1,end='')
                col = row[j]
                if col == True:
                    result += "|*|\t"
                else:
                    result += "| |\t"
            print("\n"+result + "\n")      
        
    def start(self):
        super().start()
        seats = [[False, False, False, False],
                [False, False, False, False]]
        movie = State['TICKET'].movie
        date = State['TICKET'].date
        time = State['TICKET'].time
        theatre = TheatreService.get(movie, date, time)
        seats  = theatre.seats
        print(f"Theatre for {movie} for {time} on {date} \n")

        selected_seats = []
        show_seats = True
        while True:
            if (show_seats):
                show_seats = False
                self.print_seats(seats)
            seat = input("Select your seat from available seats (E.g \"A1\")\n").upper()
            if TheatreUtils.valid_seat(seat)==True:
                row, col = TheatreUtils.split_seat(seat)
                row_index = TheatreUtils.letter_to_index(row)
                col_index = col -1
                if seats[row_index][col_index]==False:
                    seats[row_index][col_index] = True
                    selected_seats.append(seat)
                else: 
                    print("Seat already taken\n...\n")
                    continue
            else:
                print("Enter a valid seat\n...\n")
                continue
            leave = input("Do you want to enter another seat? (Enter \"yes\" to continue): ")
            if leave.lower() != "yes":
                break
            show_seats = True
            
        State['TICKET'].seats = selected_seats
        return self.navigate(Test())


            
            
        
        
        
    