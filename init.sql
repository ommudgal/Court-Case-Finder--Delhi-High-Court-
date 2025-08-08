USE courtdb;

CREATE TABLE IF NOT EXISTS `QUERY` (
  `query_num` INT NOT NULL AUTO_INCREMENT,
  `case_type` VARCHAR(45) NOT NULL,
  `case_number` VARCHAR(45) NOT NULL,
  `case_year` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`query_num`),
  UNIQUE KEY `query_num_UNIQUE` (`query_num`)
) ENGINE=InnoDB AUTO_INCREMENT=1 
  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `RESPONSE` (
  `response_no` INT NOT NULL AUTO_INCREMENT,
  `html_table` VARCHAR(9999) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`response_no`),
  UNIQUE KEY `response_no_UNIQUE` (`response_no`)
) ENGINE=InnoDB AUTO_INCREMENT=1 
  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
