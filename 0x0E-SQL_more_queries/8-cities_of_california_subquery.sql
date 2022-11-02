-- show cities of california in hbtn_0d_usa database
SELECT * FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
