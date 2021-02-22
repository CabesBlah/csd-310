#Caleb Lewandowski
#February 21, 2021
#Module 9.3 Assignment
#Purpose: To insert, update, and delete a record.

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

###############################################

#Insert into database.
cursor.execute("""INSERT INTO player (first_name, last_name, team_id)
                VALUES('Greg', 'Good', 1)""")

#Query database.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id""")
players = cursor.fetchall()

#Display results.
print("-- DISPLAYING PLAYERS AFTER INSERT --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

###############################################

#Update database.
cursor.execute("""UPDATE player
                SET team_id = 2,
                    first_name = 'Hair',
                    last_name = 'How'
                WHERE first_name = 'Greg'""")

#Query database.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id""")
players = cursor.fetchall()

#Display results.
print("\n-- DISPLAYING PLAYERS AFTER UPDATE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

###############################################

#Delete from database.
cursor.execute("""DELETE FROM player
                WHERE first_name = 'Hair'""")

#Query database.
cursor.execute("""SELECT player_id, first_name, last_name, team_name
                FROM player
                INNER JOIN team
                    ON player.team_id = team.team_id""")
players = cursor.fetchall()

#Display results.
print("\n-- DISPLAYING PLAYERS AFTER DELETE --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}\n".format(player[3]))

###############################################

#Disconnect from database.
db.close()

#Prompt exit.
input("\n\nPress any key to continue...")