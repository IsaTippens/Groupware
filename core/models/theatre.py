class Theatre:
    def __init__(self, name: str="", date: str="", time: str=""):
        self.movie = name
        self.time = time
        self.date = date
        self.seats: list[list[bool]] = []