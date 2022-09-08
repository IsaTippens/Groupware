from core.models import Theatre
from core.repositories.repository import Repository
from core.utils import load_json, save_json

class TheatreRepository(Repository):
    def __init__(self, filename: str):
        """
            seats.json
                {
                    "moviename": {
                        "date": {
                            "time": {
                                "seats":[  
                                            [0, 1, 1, 1, 0, 0], # 0 for available
                                            [0, 0, 0, 0, 0, 0], # 1 for booked
                                            [0, 0, 0, 0, 0, 0],
                                        ]
                            }
                                
                        }
                    }
                }
        """
        self.theatreFile = filename
        self.theatres: dict = {}
        self._init()

    def _init(self):
        with open(self.theatreFile, 'r') as f:
            data = load_json(f)
            self.theatres = data
        
    def get_all(self) -> list[Theatre]:
        pass

    def get(self, movie: str, date: str, time: str) -> Theatre:
        theatre = Theatre(movie, date, time)
        theatre.seats = None
        movieRecord = self.theatres.get(movie, None)
        if movieRecord is None:
            return theatre
        movieTimes = movieRecord.get(date, None)
        if movieTimes is None:
            return theatre
        theatre.seats = movieTimes.get(time, None)
        return theatre

    def add(self, value: Theatre):
        self.theatres[value.movie] = {
            value.date: {
                value.time: value.seats
            }
        }
        self._save()
    
    def _save(self):
        save_json(self.theatresFile, self.theatres)
    
    def update(self, value: Theatre):
        if self.get(value.movie, value.date, value.time).seats is None:
            self.add(value)
            return
        self.theatres[value.movie][value.date][value.time] = value.seats
        self._save()
        
    
    def delete(self, value: Theatre):
        if self.theatres.get(value.movie, None) is None:
            return
        if self.theatres[value.movie].get(value.date, None) is None:
            return
        if self.theatres[value.movie][value.date].get(value.time, None) is None:
            return
        del self.theatres[value.movie][value.date][value.time]
        self._save()

__test__ = False