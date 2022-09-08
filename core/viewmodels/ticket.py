class Ticket:
    def __init__(self):
        self.id = 0
        self.seats = []
        self.movie = None
        self.time = ""
        self.date = ""
        self.owner = ""
    
    def __str__(self):
        return f"Ticket {self.id} for {self.movie} at {self.time} for {self.owner} with {self.seats}"