-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the database
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS cities(
		id INT AUTO_INCREMENT PRIMARY KEY,
		state_id INT NOT NULL,
		name VARCHAR(256) NOT NULL
		);
