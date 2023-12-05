DELIMITER //

CREATE TRIGGER before_car_dealership_addresses_post
BEFORE INSERT
ON car_dealership_addresses FOR EACH ROW

BEGIN
    DECLARE car_dealerships_count INT;

    SELECT COUNT(*)
    INTO car_dealerships_count
    FROM car_dealership
    WHERE id = NEW.car_dealership_id;

    IF car_dealerships_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot create address for not valid car dealership';
    END IF;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER check_motor_power
BEFORE INSERT
ON motor FOR EACH ROW

BEGIN
    IF NEW.power < 100 OR NEW.power > 500 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Motor power must be between 100 and 500';
    END IF;
END //

DELIMITER ;



