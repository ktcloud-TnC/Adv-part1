# 1. Table Create
CREATE TABLE `mydb`.`fullappdjango_department` (
  `depId` INT NOT NULL AUTO_INCREMENT,
  `depName` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`depId`));

CREATE TABLE `mydb`.`fullappdjango_employee` (
  `empId` INT NOT NULL AUTO_INCREMENT,
  `empName` VARCHAR(10) NOT NULL,
  `depName` VARCHAR(10) NOT NULL,
  `joiningDate` DATE NOT NULL,
  `photoName` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`empId`));

# 2. 환경이 바뀌었을 때 (Docker, Kubernetes) 수정할 부분
fullStackDjango의 Setting.py --> DB Conn 수정 