-- lists all cities contained in the database
SELECT hbtn_0d_usa.cities.id, hbtn_0d_usa.cities.name, hbtn_0d_usa.states.name
FROM hbtn_0d_usa.cities
INNER JOIN hbtn_0d_usa.states
ON hbtn_0d_usa.cities.state_id = hbtn_0d_usa.states.id
ORDER BY hbtn_0d_usa.cities.id ASC;
