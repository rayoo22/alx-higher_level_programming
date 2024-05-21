0x0D-SQL_introduction

This directory contains various SQL scripts to perform tasks using MySQL. Below are descriptions of each task:
Task 0: List databases

File: 0-list_databases.sql

Write a script that lists all databases on your MySQL server.
Task 1: Create a database

File: 1-create_database_if_missing.sql

Write a script that creates the database hbtn_0c_0 on your MySQL server. The script should not fail if the database already exists.
Task 2: Delete a database

File: 2-remove_database.sql

Write a script that deletes the database hbtn_0c_0 on your MySQL server. The script should not fail if the database does not exist.
Task 3: List tables

File: 3-list_tables.sql

Write a script that lists all tables of a given database. The database name will be passed as an argument to the mysql command.
Task 4: First table

File: 4-first_table.sql

Write a script that creates a table named first_table in the current database with the following structure:

    id INT
    name VARCHAR(256)

If the table already exists, the script should not fail.
Task 5: Full description

File: 5-full_table.sql

Write a script that prints the full description of the table first_table from the database hbtn_0c_0. The database name will be passed as an argument to the mysql command.
Task 6: List all in table

File: 6-list_values.sql

Write a script that lists all rows of the table first_table from the database hbtn_0c_0. All fields should be printed. The database name will be passed as an argument to the mysql command.
Task 7: First add

File: 7-insert_value.sql

Write a script that inserts a new row into the table first_table of the database hbtn_0c_0 with the following values:

    id = 89
    name = 'Best School'

The database name will be passed as an argument to the mysql command.
Task 8: Count 89

File: 8-count_89.sql

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0. The database name will be passed as an argument to the mysql command.
Task 9: Full creation

File: 9-full_creation.sql

Write a script that creates a table second_table in the database hbtn_0c_0 and adds multiple rows. The table should have the following structure:

    id INT
    name VARCHAR(256)
    score INT

The script should create these records:

    id = 1, name = "John", score = 10
    id = 2, name = "Alex", score = 3
    id = 3, name = "Bob", score = 14
    id = 4, name = "George", score = 8

Task 10: List by best

File: 10-top_score.sql

Write a script that lists all records of the table second_table of the database hbtn_0c_0, displaying both the score and the name. Records should be ordered by score in descending order. The database name will be passed as an argument to the mysql command.
Task 11: Select the best

File: 11-best_score.sql

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0, displaying both the score and the name. Records should be ordered by score in descending order. The database name will be passed as an argument to the mysql command.
Task 12: Cheating is bad

File: 12-no_cheating.sql

Write a script that updates the score of "Bob" to 10 in the table second_table. Do not use Bob’s id value, only the name field. The database name will be passed as an argument to the mysql command.
Task 13: Score too low

File: 13-change_class.sql

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0. The database name will be passed as an argument to the mysql command.
Task 14: Average

File: 14-average.sql

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0. The result column name should be average. The database name will be passed as an argument to the mysql command.
Task 15: Number by score

File: 15-groups.sql

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0. The result should display the score and the number of records for this score with the label number. The list should be sorted by the number of records in descending order. The database name will be passed as an argument to the mysql command.
Task 16: Say my name

File: 16-no_link.sql

Write a script that lists all records of the table second_table of the database hbtn_0c_0 where the name is not null, displaying the score and the name. Records should be listed by descending score. The database name will be passed as an argument to the mysql command.
Task 17: Go to UTF8 (Advanced)

File: 100-move_to_utf8.sql

Write a script that converts the hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server. The script should convert the database, table first_table, and the name field in first_table to UTF8.
Task 18: Temperatures #0 (Advanced)

File: 101-avg_temperatures.sql

Import a given table dump into the hbtn_0c_0 database. Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature in descending order.
Task 19: Temperatures #1 (Advanced)

File: 102-top_city.sql

Import a given table dump into the hbtn_0c_0 database. Write a script that displays the top 3 cities by temperature during July and August, ordered by temperature in descending order.
Task 20: Temperatures #2 (Advanced)

File: 103-max_state.sql

Import a given table dump into the hbtn_0c_0 database. Write a script that displays the maximum temperature of each state, ordered by state name.
