-- lists all cities of CALIFORNIA STATE that can be found
-- in hbtn_0d_usa databsase
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name
FROM hbtn_0d_usa.cities
WHERE hbtn_0d_usa.cities.state_id = (
	SELECT hbtn_0d_usa.states.id
	FROM hbtn_0d_usa.states
	WHERE hbtn_0d_usa.states.name='California'
)
ORDER BY hbtn_0d_usa.cities.id ASC;
