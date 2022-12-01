-- list all records with a name value
-- Query that list all records with a name value

SELECT score, name FROM second_table
WHERE IF EXISTS name
ORDER BY score DESC;
