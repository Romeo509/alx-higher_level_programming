-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- give or grants a SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
