from core.repositories.repository import Repository
from core.models import Movie
from core.utils import load_json, save_json

class MovieRepository(Repository):
    def __init__(self, moviesFile: str):
        self.moviesFile = moviesFile
        self.movies: list = []
        self._init()

    def _init(self):
        with open(self.moviesFile, 'r') as f:
            data = load_json(f)
            for movie in data['movies']:
                self.movies.append(Movie(movie['name'], movie['description'], movie['type']))
        
    def get_all(self) -> list[Movie]:
        return self.movies

    def get(self,name: str) -> Movie:
        for movie in self.movies:
            if movie.name == name:
                return movie
        return None

    def add(self,value: Movie):
        self.movies.append(value)
        self._save()
    
    def _save(self):
        result = []
        for movie in self.movies:
            result.append({
                'name': movie.name,
                'type': movie.type,
                'description': movie.description
            })
        movie_dict = {'movies': result}
        save_json(self.moviesFile, movie_dict)
    
    def update(self, value: Movie):
        for movie in self.movies:
            if movie.name == value.name:
                movie.name = value.name
                movie.description = value.description
                movie.type = value.type
                self._save()
                return 
    
    def delete(self, value: Movie):
        for i in range(len(self.movies)):
            if self.movies[i].name == value.name:
                del self.movies[i]
                self._save()
                return