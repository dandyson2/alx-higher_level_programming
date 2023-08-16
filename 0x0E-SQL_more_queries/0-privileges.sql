--  a script that lists all priviledges of the MYSQL users user_0d_1 and user_0d_2
SELECT * FROM mysql.user WHERE User IN ('user_0d_1', 'user_0d_2');

