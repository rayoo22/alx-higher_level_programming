-- creates a MysQL user with all privileges, witha password
-- if they exist, the script shouldn't fail
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
