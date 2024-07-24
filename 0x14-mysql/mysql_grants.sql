-- Creates a user named holberton_user with localhost as hostname
-- and password projectcorrection280hbtn
-- holberton_user has permission to check the primary/replica status of the database

CREATE USER IF NOT EXISTS 'holberton_user'@localhost' IDENTIFIED BY 'projectcorrecion280hbtn''
GRANT REPLICATION CLIENT ON ^.^ TO 'holberton_user'@'localhost';
