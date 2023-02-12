import mysql.connector
from mysql.connector import errorcode

def show_films(cursor, title):
    """ method ot execute an inner join on all tables
        iterate over the dataset and output the results to the terminal window
    """

    # inner join query
    print("here")
    cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    #get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nStudio Name: {}\n".format(film[0], film[1], film[2]))


config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Connect to database (Step 2)
    db = mysql.connector.connect(**config)
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

    # Define cursor (Step 2.5)
    cursor = db.cursor()

    # Display films (Step 3)
    show_films(cursor, "DISPLAYING FILMS")\
    
    # Insert new movie (Step 4)
    cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Idiocracy', '2006', 84, 'Mike Judge', 1, 2)")
    
    # Display films after insert (Step 5)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien to Horror film (Step 6)
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 1")\
    
    # Display films after update (Step 7)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete the movie Gladiator (Step 8)
    cursor.execute("DELETE FROM film WHERE film_id = 1")
    
    # Display films after update (Step 9)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or passord are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()