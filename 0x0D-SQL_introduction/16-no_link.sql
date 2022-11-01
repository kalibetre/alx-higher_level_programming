-- list all records of second_table that have name record
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
