use mydb;

DROP PROCEDURE IF EXISTS insert_into_car_type;
DELIMITER //
CREATE PROCEDURE insert_into_car_type(
	IN type_name VARCHAR(45)
)
BEGIN
	INSERT INTO car_type (name) VALUES (type_name);
END //
DELIMITER ;


DROP PROCEDURE IF EXISTS insert_into_junction_table;
DELIMITER //

CREATE PROCEDURE insert_into_junction_table (
    IN car_dealership_name VARCHAR(255),
    IN user_name VARCHAR(255)
)
BEGIN
    DECLARE car_dealership_id INT;
    DECLARE user_id INT;

    SELECT id INTO car_dealership_id FROM car_dealership WHERE name = car_dealership_name;

    SELECT id INTO user_id FROM user WHERE name = user_name;

    INSERT INTO user_car_dealership (car_dealership_id, user_id) VALUES (car_dealership_id, user_id);
END //

DELIMITER ;


DROP PROCEDURE IF EXISTS insert_rows_in_package;
DELIMITER //

CREATE PROCEDURE insert_rows_in_package()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
       INSERT INTO car_type (name) VALUES (CONCAT('type', i));
       SET i = i + 1;
    END WHILE;
END //

DELIMITER ;


DROP  FUNCTION IF EXISTS calculate_statistic

DELIMITER //

CREATE FUNCTION `calculate_statistic`(
	operation VARCHAR(10)
) RETURNS int
    READS SQL DATA
BEGIN
	    DECLARE result DECIMAL DEFAULT 0.0;

    IF operation = 'min' THEN
        SELECT MIN(price) INTO result FROM advertisement;
    ELSEIF operation = 'max' THEN
        SELECT MAX(price) INTO result FROM advertisement;
    ELSEIF operation = 'avg'  THEN
        SELECT AVG(price) INTO result FROM advertisement;
  ELSEIF operation = 'sum'  THEN
        SELECT SUM(price) INTO result FROM advertisement;
    END IF;
    RETURN result;
END //

DELIMITER ;


DROP PROCEDURE  IF EXISTS get_avg;

DELIMITER //

CREATE PROCEDURE `get_avg`(
	IN operation VARCHAR(10)
)
BEGIN
	DECLARE result INT;
    set result = calculate_statistic(operation);
    SELECT result;
END

DELIMITER ;


DROP PROCEDURE IF EXISTS create_tables_from_column;
DROP VIEW IF EXISTS user_view;

DELIMITER //

CREATE PROCEDURE create_tables_from_column(
    IN custom_column_name VARCHAR(45),
    IN custom_table_name VARCHAR(45)
)
BEGIN
    DECLARE a INT DEFAULT 0;
    DECLARE b INT DEFAULT 0;
    DECLARE table_name VARCHAR(45);
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE num_columns INT;
    DECLARE column_list VARCHAR(255);
    DECLARE column_name VARCHAR(45);

    DECLARE zxcursor CURSOR FOR SELECT price FROM user_view;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    SET @query = CONCAT('CREATE OR REPLACE VIEW user_view AS SELECT ', custom_column_name, ' AS price FROM ', custom_table_name);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    OPEN zxcursor;
    my_loop: LOOP
        FETCH zxcursor INTO table_name;
        IF done THEN
            LEAVE my_loop;
        END IF;

        SET num_columns = FLOOR(1 + RAND() * 9);
		SELECT num_columns;
		SET column_list = '';
		WHILE b < num_columns DO
			SET column_name = CONCAT('column_', b + 1);
			SET column_list = CONCAT(column_list, column_name, ' INT ');
			IF b < num_columns - 1 THEN
				SET column_list = CONCAT(column_list, ', ');
			END IF;
			SET b = b + 1;
		END WHILE;
		SET b = 0;

        SET column_list = SUBSTRING(column_list, 1, LENGTH(column_list) - 1);

		SET @sql_query = CONCAT('CREATE TABLE IF NOT EXISTS ', table_name, '_', UNIX_TIMESTAMP(), ' (', column_list, ')');
		PREPARE stmt FROM @sql_query;
		EXECUTE stmt;
		DEALLOCATE PREPARE stmt;

        DROP VIEW IF EXISTS user_view;
        SET a = a + 1;
    END LOOP my_loop;

    CLOSE zxcursor;
END //

DELIMITER ;
