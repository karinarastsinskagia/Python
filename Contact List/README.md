This is a simple project for supporting users' contact lists.
It represents a one-to-many relationship, a connection between two entities

You will find a basic implementation of CRUD actions (and some extra) which have been implemented using mysql queries.

### Entities
User
Contacts

### Database
Using MysqlWorkbench environment & MySQL Community Server 9.0.1

Tables :

CREATE TABLE `python_mysql`.`users` (
  `idusers` INT NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NULL,
  PRIMARY KEY (`idusers`);

CREATE TABLE `python_mysql`.`contacts` (
  `idcontacts` INT NOT NULL AUTO_INCREMENT ,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `number` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`idcontacts`),
  INDEX `_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `python_mysql`.`users` (`idusers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
