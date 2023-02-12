import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Connect to database
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

    # Define cursor
    cursor = db.cursor()

    # Select studio table
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    # Print studio table
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))
    
    # Select genre table
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    
    # Print genre info
    print("\n-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    # Select movies with runtime less than 2 hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <120")
    short_films = cursor.fetchall()

    # Print short films
    print("\n-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))
    
    # Grab film names and director names sorted by director\
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    film_by_director = cursor.fetchall()

    # Print films by director
    print("\n--DISPLAYING Director RECORDS in Order --")
    for film in film_by_director:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

# Failed to connect to database
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or passord are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()