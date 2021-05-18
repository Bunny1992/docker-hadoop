CREATE DATABASE IF NOT EXISTS hue;
CREATE USER 'hue'@'172.16.21.13' IDENTIFIED BY 'secret';
Grant all on hue.* to 'hue'@'172.16.21.13' identified by 'secret';
Grant all on hue.* to 'root'@'172.16.21.13' identified by 'secret';
flush privileges; 
use hue;
CREATE TABLE MyGuests (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(30) NOT NULL,lastname VARCHAR(30) NOT NULL,email VARCHAR(50));
