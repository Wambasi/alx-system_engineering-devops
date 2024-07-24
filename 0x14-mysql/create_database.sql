-- create database named tyrell_corp
-- create a table named nexus6 and add atleast one entry
-- make sure that holberton_user has SELECT permissions on the table

REATE DATABASE IF NOT EXIXTS tyrell_corp;
-- to use the created database
USE tyrell_corp;

-- to create table nexus6
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255)
	);

-- add atleast one entry to the table and add a row
INSERT INTO nexus6 (name) VALUES ('Leon');

-- to grant SELECT permissions to holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
