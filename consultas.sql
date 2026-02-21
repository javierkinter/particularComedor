-- CARGA DE DATOS BASE

-- Ver las bases que hay en la conexion
SHOW DATABASES;

-- Conectarnos a nuestra base
USE comedor;

-- Mostar las tablas de la base de datos
SHOW TABLES;

DESCRIBE usuario;

SELECT * FROM usuario;

SELECT * FROM usuario LIMIT 30;

SELECT * FROM usuario WHERE tipo_usuario LIKE '%usua%';

SELECT * FROM usuario WHERE tipo_usuario LIKE '%admin%';

-- se ven los que tienen alguna observacion !!!!
SELECT * FROM usuario WHERE observacion LIKE '_%'; 

------ restricciones de usuarios
DESCRIBE restriccion_usuario;

SELECT * FROM restriccion_usuario;

-- carga de Platos Principales

DESCRIBE plato_principal;

SELECT * FROM plato_principal;

-- carga de Guarnciones

DESCRIBE guarnicion;

SELECT * FROM guarnicion;

-- carga de Bebidas

DESCRIBE bebida;

SELECT * FROM bebida;

-- carga de Postres

DESCRIBE postre;


SELECT * FROM postre;

-- carga de Menues

DESCRIBE menu;

SELECT * FROM menu;

-- carga de Pedidos

DESCRIBE pedidos;

SELECT * FROM pedidos;

--Reemplaza los id con el nombre del plato

SELECT plato_principal.nombre_plato as 'Plato principal',
guarnicion.nombre_guarnicion as 'Guarnicion',
bebida.nombre_bebida as 'Bebida',
postre.nombre_postre as 'Postre',
fecha from menu
INNER JOIN plato_principal ON menu.plato_principal_id = plato_principal.id
INNER JOIN guarnicion ON menu.guarnicion_id = guarnicion.id
INNER JOIN bebida ON menu.bebida_id = bebida.id
INNER JOIN postre ON menu.postre_id = postre.id
ORDER BY menu.id;

--Cantidad de milanesas por dia

SELECT plato_principal.nombre_plato as 'Plato principal',
guarnicion.nombre_guarnicion as 'Guarnicion', 
bebida.nombre_bebida as 'Bebida',
postre.nombre_postre as 'Postre',
menu.fecha,
count(*) as 'Cantidad'
from menu
INNER JOIN plato_principal ON menu.plato_principal_id = plato_principal.id
INNER JOIN guarnicion ON menu.guarnicion_id = guarnicion.id
INNER JOIN bebida ON menu.bebida_id = bebida.id
INNER JOIN postre ON menu.postre_id = postre.id
INNER JOIN pedidos ON pedidos.menu_id = menu.id
WHERE plato_principal.id = 1
group by fecha;

-- Se separa por dia

SELECT plato_principal.nombre_plato as 'Plato principal',
guarnicion.nombre_guarnicion as 'Guarnicion', 
bebida.nombre_bebida as 'Bebida',
postre.nombre_postre as 'Postre',
pedidos.horario as 'Horario',
menu.fecha,
count(*) as 'Cantidad'
from menu
INNER JOIN plato_principal ON menu.plato_principal_id = plato_principal.id
INNER JOIN guarnicion ON menu.guarnicion_id = guarnicion.id
INNER JOIN bebida ON menu.bebida_id = bebida.id
INNER JOIN postre ON menu.postre_id = postre.id
INNER JOIN pedidos ON pedidos.menu_id = menu.id
WHERE plato_principal.id = 1
group by fecha, horario , plato_principal.nombre_plato, guarnicion.nombre_guarnicion, bebida.nombre_bebida,
postre.nombre_postre
order by fecha,horario;

-- INNER JOIN para ver sobre una fecha ESPECÍFICA, cantidad de menues pedidos

SELECT pedidos.fecha AS 'Fecha', SUM(menu.tipo LIKE '%dia%') AS 'Cant. Menú del día', 
    SUM(menu.tipo LIKE '%pers%') AS 'Cant. Menú personalizado', 
    COUNT(pedidos.id) AS 'Cant. Total Pedidos' FROM menu
    INNER JOIN pedidos ON menu.id = pedidos.menu_id
    WHERE pedidos.fecha = '2025-11-6';