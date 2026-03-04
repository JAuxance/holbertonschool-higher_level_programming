-- Creates the database hbtn_0d_usa if it does not exist and creates the table states with an auto-incremented primary key id and a name column.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states`(`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` VARCHAR(256))