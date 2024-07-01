기본 Frontend Port : 3000

기본 Backend Port : 8000

# 1. Table Create

CREATE TABLE `mydb`.`fullAppDjango_department` (

  `depId` INT NOT NULL AUTO_INCREMENT,
  
  `depName` VARCHAR(10) NOT NULL,
  
  PRIMARY KEY (`depId`));

  

CREATE TABLE `mydb`.`fullAppDjango_employee` (

  `empId` INT NOT NULL AUTO_INCREMENT,
  
  `empName` VARCHAR(10) NOT NULL,
  
  `depName` VARCHAR(10) NOT NULL,
  
  `joiningDate` DATE NOT NULL,
  
  `photoName` VARCHAR(500) NOT NULL,
  
  PRIMARY KEY (`empId`));
  

# 2. 환경이 바뀌었을 때 (Docker, Kubernetes) 수정할 부분

api> fullStackDjango> Setting.py --> DB Conn 수정 

ui> src> component> Variable.js --> Backend 호출 주소 변경, Kubernetes일때는 서비스 명으로
