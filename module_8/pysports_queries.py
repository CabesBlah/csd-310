#Caleb Lewandowski
#February 14, 2021
#Module 8.3 Assignment
#Purpose: To query a database.

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
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()

#Display results.
print("  -- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("  Team ID: {}".format(team[0]))
    print("  Team Name: {}".format(team[1]))
    print("  Team Mascot: {}\n".format(team[2]))

#Query database.
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
players = cursor.fetchall()

#Display results.
print("\n  -- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("  Player ID: {}".format(player[0]))
    print("  First Name: {}".format(player[1]))
    print("  Last Name: {}".format(player[2]))
    print("  Team ID: {}\n".format(player[3]))

#Disconnect from database.
db.close()

#Prompt exit.
input("\n\n  Press any key to continue...")