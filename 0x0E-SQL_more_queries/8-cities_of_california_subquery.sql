-- lists all cities of CALIFORNIA STATE that can be found
-- in hbtn_0d_usa databsase
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
	SELECT states.id
	FROM states
	WHERE states.name='California'
)
ORDER BY cities.id ASC;
