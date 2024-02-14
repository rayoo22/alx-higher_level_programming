0. My Privileges
File: 0-privileges.sql
Description: This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the local server (localhost).
1. Root User
File: 1-create_user.sql
Description: This script creates the MySQL server user user_0d_1.
user_0d_1 is granted all privileges on the MySQL server.
The password for user_0d_1 is set to user_0d_1_pwd.
2. Read User
File: 2-create_read_user.sql
Description: This script creates the database hbtn_0d_2 and the user user_0d_2.
user_0d_2 is granted only SELECT privilege on the database hbtn_0d_2.
The password for user_0d_2 is set to user_0d_2_pwd.
3. Always a Name
File: 3-force_name.sql
Description: This script creates the table force_name on the MySQL server.
Table force_name has two columns: id of type INT and name of type VARCHAR(256) which cannot be null.
4. ID Can't be Null
File: 4-never_empty.sql
Description: This script creates the table id_not_null on the MySQL server.
Table id_not_null has two columns: id of type INT with a default value of 1, and name of type VARCHAR(256).
5. Unique ID
File: 5-unique_id.sql
Description: This script creates the table unique_id on the MySQL server.
Table unique_id has two columns: id of type INT with a default value of 1 and must be unique, and name of type VARCHAR(256).
6. States Table
File: 6-states.sql
Description: This script creates the database hbtn_0d_usa and the table states within it on the MySQL server.
Table states has two columns: id of type INT which is unique, auto-generated, and a primary key, and name of type VARCHAR(256).
7. Cities Table
File: 7-cities.sql
Description: This script creates the database hbtn_0d_usa and the table cities within it on the MySQL server.
Table cities has three columns: id of type INT which is unique, auto-generated, and a primary key, state_id of type INT which is a foreign key referencing id in the states table, and name of type VARCHAR(256).
8. Cities of California
File: 8-cities_of_california_subquery.sql
Description: This script lists all the cities of California found in the database hbtn_0d_usa on the MySQL server.
Results are sorted in ascending order by cities.id.
No usage of the JOIN keyword is allowed.
9. Cities by States
File: 9-cities_by_state_join.sql
Description: This script lists all cities contained in the database hbtn_0d_usa along with their respective states.
Results are sorted in ascending order by cities.id.
Only one SELECT statement is used.
10. Genre ID by Show
File: 10-genre_id_by_show.sql
Description: This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
11. Genre ID for All Shows
File: 11-genre_id_all_shows.sql
Description: This script lists all shows contained in the database hbtn_0d_tvshows.
12. No Genre
File: 12-no_genre.sql
Description: This script lists all shows contained in hbtn_0d_tvshows without a genre linked.
13. Number of Shows by Genre
File: 13-count_shows_by_genre.sql
Description: This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
14. My Genres
File: 14-my_genres.sql
Description: This script lists all genres of the show Dexter from the hbtn_0d_tvshows database.
15. Only Comedy
File: 15-comedy_only.sql
Description: This script lists all Comedy shows in the database hbtn_0d_tvshows.
16. List Shows and Genres
File: 16-shows_by_genre.sql
Description: This script lists all shows, and all genres linked to each show, from the database hbtn_0d_tvshows.

