import os

from flask import Flask
from models.database_json import Database
import views


def create_app():
    app = Flask(__name__)

    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/apresentacao", view_func=views.apresentacao_page)
    app.add_url_rule("/pessoal", view_func=views.pessoal_page)
    app.add_url_rule("/formacao", view_func=views.formacao_page)
    app.add_url_rule("/curriculum", view_func=views.curriculum_page)
    app.add_url_rule("/hobbies", view_func=views.hobbies_page)
    app.add_url_rule("/filmes", view_func=views.filmes_page)
    app.add_url_rule("/filme/<int:movie_key>", view_func=views.filme_page)
    app.add_url_rule("/new_movie", view_func=views.movie_add_page, methods=["GET", "POST"])
    app.add_url_rule("/filme/<int:movie_key>/edit", view_func=views.movie_edit_page, methods=["GET", "POST"])


    models_dir = os.path.dirname(os.path.abspath(__file__)) + "\\models"
    db = Database(os.path.join(models_dir, "movies.json"))
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)

