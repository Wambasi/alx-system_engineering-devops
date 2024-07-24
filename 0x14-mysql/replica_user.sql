-- new user should be replica_user with the host name set to %
-- password can be anything, for me its wambasivin
-- replica_user must have appropriate permissions to replicate primary MySQL server
-- holberton_user will needSELECT privileges on mysql.usertables

CREATE USER IF NOT EXISTS ;replica_user'@'%' IDENTIFIED BY 'wambasivin';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
SELECT user, Repl_slave_priv FROM mysql.user;
