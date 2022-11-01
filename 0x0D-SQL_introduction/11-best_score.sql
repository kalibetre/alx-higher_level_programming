-- show scores greater or eq to 10 from second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
