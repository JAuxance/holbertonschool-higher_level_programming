-- Creates the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Creates the table cities in the database hbtn_0d_usa if it does not exist
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities`(`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `state_id` INT NOT NULL, FOREIGN KEY (`state_id`) REFERENCES `state`(`id`))