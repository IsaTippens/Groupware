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
            self.movies = data['movies']
        
    def get_all(self):
        return self.movies

    def get(self,name: str):
        for movie in self.movies:
            if movie['name'] == name:
                return movie
        return None

    def add(self,value: Movie):
        self.movies.append(value)
        self._save_movies()
    
    def _save_movies(self):
        movie_dict = {'movies': self.movies}
        save_json(self.moviesFile, movie_dict)
    
    def update(self, value: Movie):
        for movie in self.movies:
            if movie['name'] == value['name']:
                movie['name'] = value['name']
                movie['description'] = value['description']
                movie['type'] = value['type']
                self._save_movies()
                return 
    
    def delete(self, value: Movie):
        for i in range(len(self.movies)):
            if self.movies[i]['name'] == value['name']:
                del self.movies[i]
                self._save_movies()
                return