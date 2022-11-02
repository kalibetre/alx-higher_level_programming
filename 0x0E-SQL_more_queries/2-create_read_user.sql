-- creates a new database and user
CREATE DATABASE IF NOT EXIST hbtn_0d_2;

CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO user_0d_2@localhost;
GRANT SELECT ON hbtn_0d_2 TO user_0d_2@localhost;
FLUSH PRIVILEGES;
