-- Database: student_db
-- You can create the database manually in phpMyAdmin, then run this script.

CREATE TABLE IF NOT EXISTS `students` (
  `student_id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `registration_number` VARCHAR(50) NOT NULL,
  `course` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

