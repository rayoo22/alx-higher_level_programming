-- script that lists all records of the second_table
-- display the score and name columns
-- with ordered by score (top first)
SELECT
	score, name
FROM
	second_table
ORDER BY
	score DESC;
