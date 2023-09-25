-- Usamos DROP SCHEMA IF EXISTS PARA PODER EJECUTAR TODO EL SCRIPT SIN TENER QUE ELIMINARLO MANUEALMENTE -- 
DROP SCHEMA IF exists libgetb2795599;

-- CREAMOS EL SCHEMA O BASE DE DATOS --
CREATE schema libgetb2795599;
USE libgetb2795599;

-- Creacion de la tabla categorias --
create table tbl_categorias(
	id_categoria int not null auto_increment,
    categoria varchar(40) not null,
    primary key(id_categoria)
);

-- Creacion de la tabla autores--
create table tbl_autores(
	id_autor int not null auto_increment,
    nombres varchar(25) not null,
    apellidos varchar(25) not null,
    primary key(id_autor)
);

-- Creacion de tabla libros --
create table tbl_libros(
	isbn int not null,
    titulo varchar(125) not null,
    fecha_pub date not null,
    categoria int not null,
    precio int not null,
    portada text,
    cantidad_stock int not null check (cantidad_stock >= 0),
    primary key(isbn),
    foreign key(categoria) references tbl_categorias(id_categoria)
);

-- Creacion de tabla clientes --
create table tbl_clientes(
	id_cliente int not null auto_increment,
    identificacion varchar(11) not null,
    nombres varchar(25) not null,
	apellidos varchar(25) not null,
    telefono varchar(12) not null,
    direccion varchar(100),
    correo_electronico varchar(100) not null,
    primary key(id_cliente)
);

-- INSERTAMOS LOS ELEMENTOS A LA TABLA CATEGORIAS --
INSERT INTO tbl_categorias values
	(null, 'acción y aventuras'),
    (null, 'terror'),
    (null, 'ficción'),
    (null, 'ficción moderna'),
    (null, 'suspenso'),
    (null, 'romance'),
    (null, 'narrativa'),
    (null, 'novela'),
    (null, 'poesia');
    
-- INSERTAMOS LOS ELEMENTOS A LA TABLA AUTORES --
INSERT INTO tbl_autores values
	(null, 'Marc', 'Cerasini'),
    (null, 'Julia', 'Verne'),
    (null, 'Edgar', 'Allan Poe'),
    (null, 'Mary', 'Wollstonecraft Shelley'),
    (null, 'Ben', 'Mezrich'),
    (null, 'Bram', 'Stoker'),
    (null, 'Bruno', 'Nievas'),
    (null, 'César', 'García Muñoz'),
    (null, 'Armando', 'Rodera'),
    (null, 'Jane', 'Austen'),
    (null, 'Emily', 'Bronte'),
    (null, 'Alejandro', 'Dumas'),
    (null, 'Gabriel', 'García Márquez'),
    (null, 'Nikos', 'Kazantzakis'),
    (null, 'Raymond', 'Carver'),
    (null, 'Umberto', 'Eco'),
    (null, 'Miguel', 'de Cervantes'),
    (null, 'Agatha', 'Chistie'),
    (null, 'Paulo', 'Coelho'),
    (null, 'Charles', 'Dickens'),
    (null, 'Ken', 'Follet'),
    (null, 'Federico', 'García Lorca'),
    (null, 'Ernest', 'Hemingway'),
    (null, 'Patricia', 'Highsmith'),
    (null, 'Víctor', 'Hugo'),
    (null, 'Stephen', 'King');
    
-- INSERTAMOS LOS ELEMENTOS DE LA TABLA LIBROS --
INSERT INTO tbl_libros values
	(3720, 'Operation Hell Gate', '2005/09/27', 1,  48000, '', 5),
    (7515, 'Godzilla 2000', '1997/11/11', 3, 218000, '', 2),
    --
    (3285, 'Miguel Strogoff', '2001/12/10', 1, 25000, '', 5),
    (5103, 'De la tierra a la luna', '2019/09/19', 8, 52249, '', 6),
    --
    (4681, 'El gato negro', '1997/10/12', 2, 44000, '', 9),
    (8741, 'Cuentos de terror', '2020/01/28', 2, 17000, '', 3),
    --
    (4982, 'Frankenstein', '1990/03/01', 2, 55500, '', 5),
    (1944, 'La noche de los monstruos', '2020/07/06', 2, 45599, '', 3),
    --
    (3853, 'Sexo en la luna', '2011/06/01', 4, 29500, '', 4),
    (8887, 'Los multimillonarios del bitcoin', '2019/05/21', 7, 26500, '', 8),
    --
    (4157, 'Drácula', '1999/04/10', 2, 46800, '', 15),
    (2266, 'La joya de las siete estrellas', '2016/01/21', 2, 52249, '', 7),
    --
    (4289, 'Realidad aumentada', '2001/03/13', 5, 35200, '', 3),
    (5965, 'Lo que el hielo atrapa', '2015/01/21', 8, 75900, '', 4),
    --
    (4422, 'Juicio final, sangre en el cielo', '2009/05/30', 5, 40000, '', 6),
    (7855, 'Asesinato en el campus', '2008/08/04', 8, 4079, '', 4),
    --
    (4665, 'El enigma de los vencidos', '2000/11/25', 5, 38500, '', 1),
    (5384, 'El aroma del miedo', '2017/09/05', 5, 59501, '', 1),
    --
    (5786, 'Orgullo y perjuicio', '2003/09/25', 6, 36100, '', 3),
    (9788, 'Sentido y sensibilidad', '2015/06/11', 7, 41799, '', 5),
    --
    (6034, 'Cumbres Borrascosas', '1998/11/25', 6, 60800, '', 2),
    (3852, 'Poesia completa', '2021/02/17', 9, 90249, '', 1),
    --
    (6180, 'La dama de las camelias', '1995/07/28', 6, 57600, '', 4),
    (3133, 'El collar de la reina', '2020/08/11', 8, 80749, '', 2),
    --
    (7291, 'Cien años de sledad', '1990/04/27', 7, 39500, '', 8),
    (2437, 'Crónica de una muerte anunciada', '2016/07/15', 7, 48000, '', 6),
    --
    (1282, 'Zorba, el griego', '2010/11/25', 7, 38500, '', 3),
    (9621, 'Lirio y serpiente', '2013/06/03', 7, 37905, '', 2),
    --
    (2835, 'Cathedral', '2004/08/15', 7, 25700, '', 5),
    (6339, 'Pincipiantes', '2010/05/06', 7, 85499, '', 4),
    --
    (8807, 'El nombre de la rosa', '2011/05/24', 8, 68000, '', 6),
    (2042, 'Numero cero', '2015/04/06', 8, 90249, '', 4),
	--
    (3963, 'Don Quijote de la Mancha', '1605/01/16', 8, 90000, '', 22),
	(5397, 'Rinconete y Cortadillo', '1613/01/08', 7, 38000, '', 5),
	--
	(2985, 'Asesinato en el Orient Express', '1934/09/22', 5, 36090, '', 7),
	(5437, 'El asesinato de Roger Ackroyd', '1926/11/05', 5, 64500, '', 4),
	--
	(3105, 'El Alquimista', '1988/12/17', 3, 43999, '', 13),
	(6368, 'Brida', '1990/10/02', 3, 46399, '', 7),
	--
	(7856, 'Cuento de Navidad', '1843/04/28', 8, 36099, '', 4),
	(5618, 'Grandes Esperanzas', '1861/01/01', 7, 56299, '', 2),
	--
	(1783, 'Los pilares de la Tierra', '1989/06/16', 7, 52249, '', 5),
	(6560, 'Un mundo sin fin', '2007/03/21', 4, 74590, '', 3),
	--
	(6084, 'Poeta en Nueva York', '1940/05/11', 9, 36000, '', 8),
	(6152, 'Romancero gitano', '1928/07/13', 9, 37999, '', 1),
	--
	(2827, 'Adiós a las armas', '1929/11/29', 3, 52900, '', 3),
	(7677, 'El viejo y el mar', '1952/04/17', 3, 41799, '', 6),
	--
	(2399, 'El talento de Mr. Ripley', '1955/09/24', 5, 45999, '', 10),
	(1982, 'Strangers on a Train', '1950/12/04', 5, 44399, '', 7),
	--
	(1999, 'Los Miserables', '1862/08/03', 7, 56999, '', 8),
	(1791, 'Nuestra Señora de París', '1831/11/21', 7, 56999, '', 4),
	--
	(5675, 'El resplandor', '1977/05/24', 2, 62799, '', 5),
	(5347, 'It', '1986/02/14', 2, 75999, '', 18);
    
-- Creacion de la tabla libros por autor --
CREATE TABLE tbl_libro_por_autor(
	id_autor int not null,
    isbn int not null,
    primary key(id_autor, isbn),
    foreign key(id_autor) references tbl_autores(id_autor),
    foreign key(isbn) references tbl_libros(isbn)
);

-- Creacion de la tabla pedido cliente --
create table tbl_pedido_cliente(
	id_pedido int not null auto_increment,
    nro_pedido int not null,
    id_cliente int not null,
    isbn int not null,
    fecha_pedido date not null,
    cantidad int not null default 1,
    subtotal int not null,
    primary key(id_pedido),
    foreign key(id_cliente) references tbl_clientes(id_cliente),
    foreign key(isbn) references tbl_libros(isbn)
);

-- Insertamos los elemnetos de la tabla libro por autor --
INSERT INTO tbl_libro_por_autor values
	(1, 3720),
	(1, 7515),

	(2, 3285),
	(2, 5103),

	(3, 4681),
	(3, 8741),

	(4, 4982),
	(4, 1944),

	(5, 3853),
	(5, 8887),

	(6, 4157),
	(6, 2266),

	(7, 4289),
	(7, 5965),

	(8, 4422),
	(8, 7855),

	(9, 4665),
	(9, 5384),

	(10, 5786),
	(10, 9788),

	(11, 6034),
	(11, 3852),

	(12, 6180),
	(12, 3133),

	(13, 7291),
	(13, 2437),

	(14, 1282),
	(14, 9621),

	(15, 2835),
	(15, 6339),

	(16, 8807),
	(16, 2042),

	(17, 3963),
	(17, 5397),

	(18, 2985),
	(18, 5437),

	(19, 3105),
	(19, 6368),

	(20, 7856),
	(20, 5618),

	(21, 1783),
	(21, 6560),

	(22, 6084),
	(22, 6152),

	(23, 2827),
	(23, 7677),

	(24, 2399),
	(24, 1982),

	(25, 1999),
	(25, 1791),

	(26, 5675),
	(26, 5347);
    
-- INSERTAMOS LOS ELEMNETOS DE LA TABLA CLIENTES --
INSERT INTO tbl_clientes values
	(null, '1033178129', 'Geronimo', 'Trujillo', '3104049506', 'Calle 79 #44-38', 'gtutos3@gmail.com'),
    (null, '1195678128', 'David', 'Ospina', '3156478910', 'Cra 75 #87-00', 'dospina2@gmail.com'),
    (null, '1287809867', 'Yerry', 'Mina', '3206759807', 'Cra 42 #90-13', 'yerrym13@gmail.com'),
    (null, '1298085632', 'Juan Fernando', 'Quintero', '3156708723', 'Calle 65sur #42-45', 'jfquinter0@gmail.com'),
    (null, '1028156234', 'Juan Guillermo', 'Cuadrado', '3126745687', 'Cra 15 #65-12', 'cuadradojg@gmail.com'),
    (null, '1023894378', 'Yimmy', 'Chará', '3187259018', 'Calle 75 #44-33', 'charayimmy9823@gmail.com');
    
-- ELIMINAMOS 3 DE LOS 6 CLIENTES --
DELETE FROM tbl_clientes
	where id_cliente in (2, 4, 5);
    
-- AGREGAMOS LOS ELEMENTOS DE LA TABLA PEDIDO CLIENTE --
INSERT INTO tbl_pedido_cliente values
	(null, 1, 1, 6368, '2023/06/15', 5, 231995),
    (null, 2, 3, 5675, '2023/06/19', 2, 125598),
    (null, 3, 6, 5347, '2023/06/28', 4, 303996);

    
-- MOSTRAMOS TODAS LAS TABLAS ANTERIORMENTE CREADAS --
select * from tbl_categorias;
select * from tbl_autores;
select * from tbl_libros;
select * from tbl_libro_por_autor;
select * from tbl_clientes;
select * from tbl_pedido_cliente;