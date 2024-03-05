-- script that lists all records of the second_table
-- displaying score and name
-- records listed in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
