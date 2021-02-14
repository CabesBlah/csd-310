-- Caleb Lewandowski
-- February 14, 2021
-- Module 8.2 Assignment
-- Purpose: To initialize the database.

-- Create a user. If user already exists, drop it.
DROP USER IF EXISTS 'pysports_user'@'localhost';
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '12345678';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

-- Drop tables player and team if they exist.
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

-- Create the table team.
CREATE TABLE team (
    team_id     INT         NOT NULL    AUTO_INCREMENT,
    team_name   VARCHAR(75) NOT NULL,
    mascot      VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

-- Create the table player.
CREATE TABLE player (
    player_id   INT         NOT NULL    AUTO_INCREMENT,
    first_name  VARCHAR(75) NOT NULL,
    last_name   VARCHAR(75) NOT NULL,
    team_id     INT         NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

-- Insert teams into the table team.
INSERT INTO team(team_name, mascot)
    VALUES('Team Fire', 'Phoenix');
INSERT INTO team(team_name, mascot)
    VALUES('Team Water', 'Fish');

-- Insert players into the table player.
INSERT INTO player(first_name, last_name, team_id)
    VALUE('Axel', 'Air', (SELECT team_id FROM team WHERE team_name = 'Team Fire'));
INSERT INTO player(first_name, last_name, team_id)
    VALUE('Bob', 'Bank', (SELECT team_id FROM team WHERE team_name = 'Team Fire'));
INSERT INTO player(first_name, last_name, team_id)
    VALUE('Caleb', 'Coal', (SELECT team_id FROM team WHERE team_name = 'Team Fire'));
INSERT INTO player(first_name, last_name, team_id)
    VALUE('Doug', 'Dude', (SELECT team_id FROM team WHERE team_name = 'Team Water'));
INSERT INTO player(first_name, last_name, team_id)
    VALUE('Earl', 'Eat', (SELECT team_id FROM team WHERE team_name = 'Team Water'));
INSERT INTO player(first_name, last_name, team_id)
    VALUE('Fred', 'Fog', (SELECT team_id FROM team WHERE team_name = 'Team Water'));