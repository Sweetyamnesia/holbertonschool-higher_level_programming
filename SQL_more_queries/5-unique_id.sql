-- Script that creates the table unique_id on my MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DISTINCT VALUE,
	name VARCHAR(256) 
);
