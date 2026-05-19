from multiprocessing.dummy import connection
import sqlite3 as dbapi2
from models.movie import Movie


class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile
        self.create_table()

    def create_table(self):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS MOVIE (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TITLE VARCHAR (80) NOT NULL UNIQUE,
                YEAR INTEGER)""")

            cursor.execute(
                "INSERT OR IGNORE INTO MOVIE (TITLE, YEAR) VALUES (?, ?)",
                ("The Matrix", 1999),
            )
            cursor.execute(
                "INSERT OR IGNORE INTO MOVIE (TITLE, YEAR) VALUES (?, ?)",
                ("Inception", 2010),
            )
            connection.commit()

    def get_movies(self):
        movies = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, YEAR FROM MOVIE ORDER BY ID"
            cursor.execute(query)
            for movie_key, title, year in cursor:
                movies.append((movie_key, Movie(title, year)))
        return movies  # <-- AGORA ESTÁ FORA DO FOR!

    # NOVO MÉTODO PARA OS LINKS FUNCIONAREM
    def get_movie(self, movie_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT TITLE, YEAR FROM MOVIE WHERE (ID = ?)"
            cursor.execute(query, (movie_key,))
            result = cursor.fetchone()
            if result is None:
                return None
            title, year = result
            return Movie(title, year=year)


    def add_movie(self, movie):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO MOVIE (TITLE, YEAR) VALUES (?, ?)"
            cursor.execute(query, (movie.title, movie.year))
            connection.commit()
            movie_key = cursor.lastrowid
        return movie_key
    
    def update_movie(self, movie_key, movie):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            # O comando UPDATE altera os valores da linha onde o ID corresponde à nossa movie_key
            query = "UPDATE MOVIE SET TITLE = ?, YEAR = ? WHERE ID = ?"
            cursor.execute(query, (movie.title, movie.year, movie_key))
            connection.commit()