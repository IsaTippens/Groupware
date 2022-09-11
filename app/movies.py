from app.screen.titled_screen import TitledScreen
from app.globals import MovieService
from app.globals import State
from app.time import Times 
class MovieScreen(TitledScreen):
    def __init__(self):
        super().__init__("Movies")

    def start(self):
        super().start()
        count = 1
        movies = MovieService.get_all()
        for movie in movies:
            print("Theatre "+ str(count))
            print(movie.name)
            print(movie.description, "\n")
            count= count+1
        while True:
            print("Enter theater number for the movie selection or 0 to return home:")
            num = input().strip() # incase spaces are included at the beginning or end
            if not num.isdigit():
                print("Enter a number listed")
                continue
            num = int(num)
            if num > len(movies) or num < 0:
                print("Select a valid option")
                continue

            if num==0: 
                return self.goBack()
            else:  
                Selection = movies[num-1]
                State["MOVIE"] = Selection
                State["TICKET"].movie = Selection
                return self.navigate(Times())
