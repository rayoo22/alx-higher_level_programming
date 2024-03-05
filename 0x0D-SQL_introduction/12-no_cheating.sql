-- updates the score of Bob to to 10 in the second_table
-- without usinf Bob's id, only the name field
UPDATE second_table
SET score=10
WHERE name="Bob"
