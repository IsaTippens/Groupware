from app.screen.titled_screen import TitledScreen
from core.utils import TheatreUtils
from app.globals import State, TheatreService
from app.Test import Test


class SelectSeatsScreen(TitledScreen):
    def __init__(self):
        super().__init__('SelectSeats')
        
    def start(self):
        super().start()
        seats = [[False, False, False, False],
                [False, False, False, False]]
        movie = State['TICKET'].movie
        date = State['TICKET'].date
        time = State['TICKET'].time
        theatre = TheatreService.get(movie, date, time)
        seats  = TheatreService.generate_seats(2,4)
        print(seats)
        print(f"Theatre for {movie} for {time} on {date} \n")
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
            
        valid = 0
        while valid==0:
            seat = input("Select your seat from available seats\n")
            if TheatreUtils.valid_seat(seat)==True:
                selected_seats = []
                row, col = TheatreUtils.split_seat(seat)
                row_index = TheatreUtils.letter_to_index(row)
                col_index = col -1
                print(seats)
                if seats[row_index][col_index]==False:
                    seats[row_index][col_index] = True
                    selected_seats.append(seat)
                    State['TICKET'].seats = selected_seats
                    # theatre = TheatreService.get(movie, date, time)
                    # seats = theatre.seats
                    # print(seats)
                else: 
                    print("Seat already taken\n...\n")
                valid=1

            else:
                print("Enter a valid seat\n...\n")
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
                    

        proceed = 0
        while proceed==0:
            Question = input("Do you wish to select another seat. Yes or No\n")
            if Question.upper() == "YES":
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
                seat = input("Select your seat number from available seats\n")
                if TheatreUtils.valid_seat==True:
                    selected_seats = []
                    row, col = TheatreUtils.split_seat(seat)
                    row_index = TheatreUtils.letter_to_index(row)
                    col_index = col -1
                    if seats[row_index][col_index]==False:
                        seats[row_index][col_index] = True
                        selected_seats.append(seat)
                        State['TICKET'].seats = selected_seats
                        # theatre = TheatreService.get(movie, date, time)
                        # seats = theatre.seats
                        # print(seats)
                    else: 
                        print("Seat already taken\n...\n")
                else: 
                    print("Enter a valid seat\n...")
            elif Question.upper() == "NO":
                proceed =1
            else:
                print("Enter a valid input\n...")
                
                
        return self.navigate(Test())


            
            
        
        
        
    