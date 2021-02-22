#Caleb Lewandowski
#February 21, 2021
#Module 9.2 Assignment
#Purpose: To inner join tables.

#Import classes.
import mysql.connector
from mysql.connector import errorcode

#Create dictionary config.
config = {
    "user": "pysports_user",
    "password": "12345678",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

#Connect to database.
db = None
try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist.")
    else:
        print(err)
    db.close()
    exit()

#Create cursor.
cursor = db.cursor()

#Query database.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id""")
players = cursor.fetchall()

#Display results.
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

#Disconnect from database.
db.close()

#Prompt exit.
input("\n\nPress any key to continue...")