-- lists all rows leaving rows without name value
SELECT score, name FROM second_table WHERE name IS NOT NULL;
