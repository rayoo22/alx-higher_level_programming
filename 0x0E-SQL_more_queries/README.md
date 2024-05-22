SQL More Queries

This repository contains scripts for various SQL tasks related to MySQL server management, user privileges, database creation, and table manipulations. Each task is described below along with the corresponding file in the 0x0E-SQL_more_queries directory.
Tasks
0. My privileges!

File: 0-privileges.sql

This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the localhost server.
1. Root user

File: 1-create_user.sql

This script creates the MySQL server user user_0d_1 with all privileges. The password for user_0d_1 is set to user_0d_1_pwd. If the user already exists, the script does not fail.
2. Read user

File: 2-create_read_user.sql

This script creates the database hbtn_0d_2 and the user user_0d_2 with only the SELECT privilege on the hbtn_0d_2 database. The password for user_0d_2 is set to user_0d_2_pwd. If the database or user already exists, the script does not fail.
3. Always a name

File: 3-force_name.sql

This script creates the table force_name with the following structure:

    id INT
    name VARCHAR(256) NOT NULL

The database name is passed as an argument to the MySQL command. If the table already exists, the script does not fail.
4. ID can't be null

File: 4-never_empty.sql

This script creates the table id_not_null with the following structure:

    id INT DEFAULT 1
    name VARCHAR(256)

The database name is passed as an argument to the MySQL command. If the table already exists, the script does not fail.
5. Unique ID

File: 5-unique_id.sql

This script creates the table unique_id with the following structure:

    id INT DEFAULT 1 UNIQUE
    name VARCHAR(256)

The database name is passed as an argument to the MySQL command. If the table already exists, the script does not fail.
6. States table

File: 6-states.sql

This script creates the database hbtn_0d_usa and the table states with the following structure:

    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY
    name VARCHAR(256) NOT NULL

If the database or table already exists, the script does not fail.
7. Cities table

File: 7-cities.sql

This script creates the table cities in the hbtn_0d_usa database with the following structure:

    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY
    state_id INT NOT NULL (FOREIGN KEY references states.id)
    name VARCHAR(256) NOT NULL

If the table already exists, the script does not fail.
8. Cities of California

File: 8-cities_of_california_subquery.sql

This script lists all cities of California found in the hbtn_0d_usa database. The results are sorted in ascending order by cities.id. The database name is passed as an argument to the MySQL command.
9. Cities by States

File: 9-cities_by_state_join.sql

This script lists all cities contained in the hbtn_0d_usa database. Each record displays: cities.id - cities.name - states.name. The results are sorted in ascending order by cities.id. The database name is passed as an argument to the MySQL command.
10. Genre ID by show

File: 10-genre_id_by_show.sql

This script lists all shows in the hbtn_0d_tvshows database that have at least one genre linked. Each record displays: tv_shows.title - tv_show_genres.genre_id. The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. The database name is passed as an argument to the MySQL command.
11. Genre ID for all shows

File: 11-genre_id_all_shows.sql

This script lists all shows in the hbtn_0d_tvshows database. Each record displays: tv_shows.title - tv_show_genres.genre_id. If a show doesn’t have a genre, NULL is displayed. The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. The database name is passed as an argument to the MySQL command.
12. No genre

File: 12-no_genre.sql

This script lists all shows in the hbtn_0d_tvshows database without a genre linked. Each record displays: tv_shows.title - tv_show_genres.genre_id. The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. The database name is passed as an argument to the MySQL command.
13. Number of shows by genre

File: 13-count_shows_by_genre.sql

This script lists all genres from the hbtn_0d_tvshows database and displays the number of shows linked to each. Each record displays: <TV Show genre> - <Number of shows linked to this genre>. The results are sorted in descending order by the number of shows linked. The database name is passed as an argument to the MySQL command.
14. My genres

File: 14-my_genres.sql

This script lists all genres of the show Dexter from the hbtn_0d_tvshows database. Each record displays: tv_genres.name. The results are sorted in ascending order by the genre name. The database name is passed as an argument to the MySQL command.
15. Only Comedy

File: 15-comedy_only.sql

This script lists all Comedy shows in the hbtn_0d_tvshows database. Each record displays: tv_shows.title. The results are sorted in ascending order by the show title. The database name is passed as an argument to the MySQL command.
16. List shows and genres

File: 16-shows_by_genre.sql

This script lists all shows and all genres linked to each show in the hbtn_0d_tvshows database. If a show doesn’t have a genre, NULL is displayed in the genre column. Each record displays: tv_shows.title - tv_genres.name. The results are sorted in ascending order by the show title and genre name. The database name is passed as an argument to the MySQL command.
17. Not my genre

File: 17-not_my_genre.sql

This script lists all genres not linked to the show Dexter from the hbtn_0d_tvshows database. Each record displays: tv_genres.name. The results are sorted in ascending order by the genre name. The database name is passed as an argument to the MySQL command.
