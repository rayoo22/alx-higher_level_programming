-- lists all cities of california without using the JOIN KEYWORD
SELECT id, name
FROM hbtn_0d_usa.cities
WHERE id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California';)
ORDER BY hbtn_0d_usa.cities.id ASC
