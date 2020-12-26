/*
    Script para la creación de tablas de la Base de Datos


    ESTE SCRIPT SE DEBE EJECUTAR CON EL SHELL DE POSTGRESQL
    O EN SU DEFECTO, SE PUEDE IR INGRESANDO A MANO EN EL SHELL
    
    
    
    Para revisar las tablas en el shell, usar \d
    por ejemplo: \d rendición
*/

/*
    CLIENTE
*/
CREATE TABLE cliente (
    client_id  Serial,
    rut        VARCHAR(16) NOT NULL,
    nombre     VARCHAR(30) NOT NULL,
    apellido   VARCHAR(30) NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( client_id );

/*
    EMPLEADO
*/

CREATE TABLE empleado (
    empl_id   INTEGER NOT NULL,
    rut       VARCHAR(16) NOT NULL,
    nombre    VARCHAR(30) NOT NULL,
    apellido  VARCHAR(30) NOT NULL
);

ALTER TABLE empleado ADD CONSTRAINT empleados_pk PRIMARY KEY ( empl_id );

/*
    rendicion
*/

CREATE TABLE rendicion (
    ren_id              INTEGER NOT NULL,
    fecha               VARCHAR(30) NOT NULL,
    puntaje             INTEGER NOT NULL,
    estado              CHAR(1) NOT NULL,
    observaciones       VARCHAR(50),
    empleado_empl_id    INTEGER NOT NULL,
    cliente_client_id   INTEGER NOT NULL,
    tipo_examen_tip_id  INTEGER NOT NULL
);

ALTER TABLE rendicion ADD CONSTRAINT rendicion_pk PRIMARY KEY ( ren_id );

/*
    TIPO EXAMEN
*/

CREATE TABLE tipo_examen (
    tip_id  INTEGER NOT NULL,
    titulo  VARCHAR(30) NOT NULL,
    grado   VARCHAR(30) NOT NULL,
    precio  INTEGER NOT NULL
);

ALTER TABLE tipo_examen ADD CONSTRAINT tipo_examen_pk PRIMARY KEY ( tip_id );

/*
    LLAVES FORANEAS DE RENDICION
*/

ALTER TABLE rendicion
    ADD CONSTRAINT rendicion_cliente_fk FOREIGN KEY ( cliente_client_id )
        REFERENCES cliente ( client_id );

ALTER TABLE rendicion
    ADD CONSTRAINT rendicion_empleado_fk FOREIGN KEY ( empleado_empl_id )
        REFERENCES empleado ( empl_id );

ALTER TABLE rendicion
    ADD CONSTRAINT rendicion_tipo_examen_fk FOREIGN KEY ( tipo_examen_tip_id )
        REFERENCES tipo_examen ( tip_id );