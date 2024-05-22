-- lists all cities of california without using the JOIN KEYWORD
SELECT id, name FROM cities WHERE id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY cities.id ASC;
