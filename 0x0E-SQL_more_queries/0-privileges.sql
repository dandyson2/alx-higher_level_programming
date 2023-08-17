--  a script that lists all priviledges of the MYSQL users user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

REVOKE ALL ON *.* FROM 'user_0d_1'@'localhost';

-- Grant missing privileges (replace 'privilege_name' with the actual privilege to grant)
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
