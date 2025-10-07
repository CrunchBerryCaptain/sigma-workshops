from pprint import pprint

from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def get_db_connection() -> connection:
    """Return a live connection to the DB"""
    return connect(
        dbname="streaming",
        cursor_factory=RealDictCursor,
    )


def get_media(conn: connection, genre: str, media_type: str, release_year: int) -> list:
    """Fetch title and release year of media items from DB"""

    # create a cursor for our connection pipe
    cursor = conn.cursor()

    # let's define our SQL query to get the data we want
    sql_query = """
    SELECT 
        m.title, 
        m.release_year,
        mt.media_type_name
    FROM media m

    JOIN media_type mt
        ON m.media_type_id = mt.media_type_id
    
    JOIN media_genre_link as mgl
    ON m.media_id = mgl.media_id
    JOIN genre as g
    ON g.genre_id = mgl.genre_id

    WHERE genre=%s 
    AND
        mt.media_type_name = %s
    ;
    """

    cursor.execute(sql_query, (genre, media_type, release_year))

    rows = cursor.fetchall()

    cursor.close()

    return rows


if __name__ == "__main__":
    conn = get_db_connection()
    # do lots of different queries here
    pprint(get_media(conn, "show"))
    conn.close()
