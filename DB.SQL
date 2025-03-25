create DATABASE visualshield;

USE visualshield;

CREATE TABLE logs_camera (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME,
    erro VARCHAR(255),
    epi_faltando VARCHAR(255)
);
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (1, '2025-03-24 13:30:00', 'sem capacete', 'capacete');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (2, '2025-01-21 14:24:32', 'sem capacete', 'capacete');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (3,'2024-11-13 09:46:54', 'sem capacete', 'capacete');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (4,'2025-04-29 16:14:21', 'sem luva', 'luva');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (5,'2025-06-01 08:05:13', 'sem oculos', 'oculos');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (6,'2025-08-15 15:55:45', 'sem luva', 'luva');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (7,'2025-11-30 13:42:34', 'sem oculos', 'oculos');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (8,'2025-11-16 10:17:12', 'sem capacete', 'capacete');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (9,'2025-12-22 08:27:00', 'sem luva', 'luva');
INSERT INTO `visualshield`.`logs_camera` (`id`, `data_hora`, `erro`, `epi_faltando`) VALUES (10, '2024-02-24 14:12:00', 'sem luva', 'luva');
