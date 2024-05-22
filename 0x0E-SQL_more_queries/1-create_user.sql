-- create user user_0d_1 with all privileges, and a password set
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED WITH 'caching_sha2_password' BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
