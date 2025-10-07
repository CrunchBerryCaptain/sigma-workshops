from flask import Flask, request

from database import get_db_connection, get_media

app = Flask(__name__)
conn = get_db_connection()


@app.route("/media", methods=["GET"])
def movies():
    """..."""
    media_type = request.args.get("media_type", "movie")

    media = get_media(conn, media_type)

    return media


@app.route("/genre/<genre_name>", methods=["GET"])
def genre(genre_name: str):
    media_type = request.args.get("media_type", "movie")
    release_year = request.args.get("release_year", "2000")

    media = get_media(conn, genre, media_type, release_year)

    return media


if __name__ == "__main__":
    app.run(port=8080, debug=True)
