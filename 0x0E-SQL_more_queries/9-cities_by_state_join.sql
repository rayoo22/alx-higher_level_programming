-- lists all cities, displaying cities.id, cities.name, states.name
-- sorting in asc by cities.id
-- using one SELECT keyword
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
