-- add bonus procedure
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
    DECLARE project_id INT;
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    INSERT INTO corrections (user_id, project_name, score) VALUES (user_id, project_id, score);
end //


DELIMITER ;