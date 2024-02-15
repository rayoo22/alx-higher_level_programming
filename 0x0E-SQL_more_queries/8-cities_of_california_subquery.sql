-- lists all cities of CALIFORNIA STATE that can be found
-- in hbtn_0d_usa databsase
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name
FROM hbtn_0d_usa.cities
WHERE state_id = (
	SELECT id
	FROM hbtn_0d_usa.states
	WHERE name='California'
)
ORDER BY hbtn_0d_usa.cities.id ASC;
