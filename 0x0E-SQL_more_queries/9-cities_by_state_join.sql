-- lists all cities of california without using the JOIN KEYWORD
SELECT cities.id, cities.name, states.name FROM hbtn_0d_usa.cities INNER JOIN hbtn_0d_usa.states ON cities.state_id = states.id ORDER BY cities.id ASC;
