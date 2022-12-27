-- Script that creates a database and table
-- Query to create the database 'hbtn_0d_usa' and the table 'states'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
