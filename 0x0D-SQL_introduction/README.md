To solve these SQL tasks, you need to create SQL scripts that perform specific operations on a MySQL database. Here's a breakdown of each task along with the corresponding solution:

List databases: Create a SQL script that lists all databases on the MySQL server.

Solution: Use SHOW DATABASES; in your SQL script.
Create a database: Write a script that creates a database named hbtn_0c_0 if it doesn't already exist.

Solution: Use CREATE DATABASE IF NOT EXISTS hbtn_0c_0; in your SQL script.
Delete a database: Write a script that deletes the hbtn_0c_0 database if it exists.

Solution: Use DROP DATABASE IF EXISTS hbtn_0c_0; in your SQL script.
List tables: Create a script that lists all tables in a specified database.

Solution: Use SHOW TABLES; in your SQL script after selecting the desired database.
First table: Write a script that creates a table named first_table with specified columns in the current database.

Solution: Use CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256)); in your SQL script.
Full description: Create a script that prints the full description of the first_table.

Solution: Use SHOW CREATE TABLE first_table; in your SQL script.
List all in table: Write a script that lists all rows of first_table.

Solution: Use SELECT * FROM first_table; in your SQL script.
First add: Create a script that inserts a new row into first_table.

Solution: Use INSERT INTO first_table (id, name) VALUES (89, 'Best School'); in your SQL script.
Count 89: Write a script that displays the number of records with id = 89 in first_table.

Solution: Use SELECT COUNT(*) FROM first_table WHERE id = 89; in your SQL script.
Full creation: Script to create a table named second_table and insert multiple rows.

Solution: Use CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT); to create the table and then multiple INSERT INTO second_table statements to add rows.
List by best: Script to list all records of second_table ordered by score.

Solution: Use SELECT * FROM second_table ORDER BY score DESC;.
Select the best: Script to list records with a score >= 10 from second_table.

Solution: Use SELECT * FROM second_table WHERE score >= 10 ORDER BY score DESC;.
Cheating is bad: Script to update the score of Bob to 10 in second_table without using Bob's id.

Solution: Use UPDATE second_table SET score = 10 WHERE name = 'Bob';.
Score too low: Script to remove records with a score <= 5 from second_table.

Solution: Use DELETE FROM second_table WHERE score <= 5;.
Average: Script to compute the average score of all records in second_table.

Solution: Use SELECT AVG(score) AS average FROM second_table;.
Number by score: Script to list the number of records with the same score in second_table.

Solution: Use SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;.
Go to UTF8: Script to convert the hbtn_0c_0 database, first_table, and the name field to UTF8.

Solution: Use ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; to convert the database and similar commands for the table and field.
Temperatures #0: Script to display the average temperature by city ordered by temperature.

Solution: Use SQL queries to calculate the average temperature for each city and order the results accordingly.
Temperatures #1: Script to display the top 3 cities by temperature during July and August.

Solution: Write SQL queries to filter data for July and August, calculate the average temperature for each city, and then order the results to get the top 3 cities.
Temperatures #2: Script to display the max temperature of each state ordered by state name.

Solution: Write SQL queries to calculate the max temperature for each state and order the results by state name.
