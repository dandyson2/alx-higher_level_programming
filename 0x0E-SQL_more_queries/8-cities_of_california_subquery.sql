--  a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
USE hbtn_0d_usa;

-- Fetch the state_id for California from the states table
SET @california_state_id := (SELECT id FROM states WHERE name = 'California');

-- List all cities of California sorted by cities.id
SELECT * FROM cities
WHERE state_id = @california_state_id
ORDER BY id ASC;

