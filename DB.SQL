create DATABASE visualshield;

USE visualshield;

CREATE TABLE logs_camera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME,
    erro VARCHAR(255),
    epi_faltando VARCHAR(255)
);
