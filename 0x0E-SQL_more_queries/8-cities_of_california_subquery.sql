-- Script to list all cities of California
-- Query to list all cities of California that can be found
SELECT id,name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California") ORDER BY ASC cities.id;
