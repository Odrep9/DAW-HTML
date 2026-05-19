import json
import os

from models.movie import Movie


class Database:

    def __init__(self, dbfile):
        self.dbfile = dbfile

        # Se o ficheiro JSON não existir, cria-o vazio
        if not os.path.exists(self.dbfile):
            with open(self.dbfile, "w") as file:
                json.dump([], file)

    # LER TODOS OS FILMES
    def get_movies(self):

        with open(self.dbfile, "r") as file:
            data = json.load(file)

        movies = []

        for movie in data:
            movie_key = movie["id"]

            movie_obj = Movie(movie["title"], movie["year"])

            movies.append((movie_key, movie_obj))

        return movies

    # LER APENAS UM FILME
    def get_movie(self, movie_key):

        with open(self.dbfile, "r") as file:
            data = json.load(file)

        for movie in data:

            if movie["id"] == movie_key:

                return Movie(movie["title"], movie["year"])

        return None

    # ADICIONAR FILME
    def add_movie(self, movie):

        with open(self.dbfile, "r") as file:
            data = json.load(file)

        # gerar novo ID
        if data:
            new_id = max(m["id"] for m in data) + 1
        else:
            new_id = 1

        new_movie = {"id": new_id, "title": movie.title, "year": movie.year}

        data.append(new_movie)

        with open(self.dbfile, "w") as file:
            json.dump(data, file, indent=4)

        return new_id

    # EDITAR FILME
    def update_movie(self, movie_key, movie):

        with open(self.dbfile, "r") as file:
            data = json.load(file)

        for m in data:

            if m["id"] == movie_key:

                m["title"] = movie.title
                m["year"] = movie.year

        with open(self.dbfile, "w") as file:
            json.dump(data, file, indent=4)

    # APAGAR FILME
    def delete_movie(self, movie_key):

        with open(self.dbfile, "r") as file:
            data = json.load(file)

        data = [m for m in data if m["id"] != movie_key]

        with open(self.dbfile, "w") as file:
            json.dump(data, file, indent=4)
