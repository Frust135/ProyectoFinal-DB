/*
    Script para la inserción de datos en la Base de Datos


    ESTE SCRIPT SE DEBE EJECUTAR CON EL SHELL DE POSTGRESQL
    O EN SU DEFECTO, SE PUEDE IR INGRESANDO A MANO EN EL SHELL
    
*/

/*
    TIPO EXAMEN
*/

INSERT INTO tipo_examen(tip_id, titulo, grado, precio) VALUES (1,'Java Nivel 1', 'Básico', 13900);

INSERT INTO tipo_examen(tip_id, titulo, grado, precio) VALUES (2,'Java Nivel 2', 'Intermedio', 16900);

INSERT INTO tipo_examen(tip_id, titulo, grado, precio) VALUES (3,'Java Nivel 3', 'Experto', 19900);

INSERT INTO tipo_examen(tip_id, titulo, grado, precio) VALUES (4,'Oracle Básico', 'Básico', 13900);

INSERT INTO tipo_examen(tip_id, titulo, grado, precio) VALUES (5,'Oracle Intermedio', 'Intermedio', 16900);

INSERT INTO tipo_examen(tip_id, titulo, grado, precio) VALUES (6,'Oracle Experto', 'Experto', 19900);

/*
    EMPLEADO
*/

INSERT INTO empleado(empl_id, rut, nombre, apellido) VALUES (1,'20.543.572-2', 'Juan', 'Pérez');

INSERT INTO empleado(empl_id, rut, nombre, apellido) VALUES (2,'19.564.232-3', 'Karen', 'Corama');

INSERT INTO empleado(empl_id, rut, nombre, apellido) VALUES (3,'20.312.542-k', 'Hugo', 'Palma');

INSERT INTO empleado(empl_id, rut, nombre, apellido) VALUES (4,'18.310.189-0', 'Francisca', 'Salas');

INSERT INTO empleado(empl_id, rut, nombre, apellido) VALUES (5,'20.312.610-9', 'Patricio', 'Saez');

INSERT INTO empleado(empl_id, rut, nombre, apellido) VALUES (6,'19.895.533-0', 'Ester', 'Valderrama');