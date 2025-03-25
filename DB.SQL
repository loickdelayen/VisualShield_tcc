create DATABASE visualshield;

USE visualshield;

CREATE TABLE logs_camera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME,
    erro VARCHAR(255),
    epi_faltando VARCHAR(255)
);
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES ('1', '2025-03-24 13:30:00', 'sem capacete', 'capacete');