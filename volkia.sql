create database volkia;
use volkia;

-- use master
-- drop database volkia

create table carrier(
	CarrierID int not null primary key,
	name varchar(16) not null,
	Capacity int not null
);

create table costos(
	CarrierID int not null,
	Zona varchar(64) not null,
	Costo int not null,
	Tiempo_de_entrega int not null
);

create table cantidad_de_envios(
	Zona varchar(64) not null,
	Mes int not null,
	Cantidad_de_envios int not null
);

alter table costos
add constraint fk_costos_carrier
foreign key (CarrierID) references carrier(CarrierID)

insert into carrier (CarrierID, name, Capacity) values 
	('1', 'Carrier A', '10000'),
	('2', 'Carrier B', '10000'),
	('3', 'Carrier C', '3000');

insert into costos(CarrierID, Zona, Costo, Tiempo_de_entrega) values (
	'1', 'AMBA', '10', '3'),
	('1', 'Bs As', '20', '5'),
	('1', 'Resto', '50', '7'),
	('1', 'AMBA', '15', '2'),
	('1', 'Bs As', '19', '4'),
	('1', 'Resto', '55', '6'),
	('1', 'AMBA', '20', '1'
);

insert into cantidad_de_envios(Zona, Mes, Cantidad_de_envios) values (
	'AMBA', '1', '40000'),
	('Bs As', '1', '50000'),
	('Resto', '1', '60000'
);

-- join por mes (tambien zona) teniendo en cuenta costos.costo en una suma, envios.mes por carrierid y carrier.name obtenido por carrier.id
--  Obtener para el mes 1 cuánto costaría enviar con cada carrier los envíos de la tabla Cantidad de envíos

-- NO_ES_CORRECTO_AL_PEDIDO_DEL_EJERCICIO
-- SELECT ce.mes, ca.CarrierID, ce.Zona, SUM(ce.Cantidad_de_envios)
-- FROM Cantidad_de_envios ce
-- INNER JOIN Costos co ON ce.Zona = co.Zona
-- INNER JOIN Carrier ca ON co.CarrierID = ca.CarrierID
-- group by ce.Mes

-- SELECT mes, sum(Cantidad_de_envios)
-- from cantidad_de_envios ce
-- INNER JOIN Costos co ON ce.Zona = co.Zona
-- INNER JOIN Carrier ca ON co.CarrierID = ca.CarrierID
-- where Mes = '1'
-- group by ce.Zona;




-- SELECT SUM(cantidad_de_envios.Cantidad_de_envios * costos.costo) 
-- FROM cantidad_de_envios
-- INNER JOIN costos
-- ON (carrier.CarrierID = costos.carrierID)
-- WHERE cantidad_de_envios.mes=1


select * from cantidad_de_envios


-- SELECT cantidad_de_envios, c.Zona, sum(ce.Cantidad_de_envios * c.Costo)
-- FROM cantidad_de_envios ce
-- INNER JOIN costos c
-- ON cantidad_de_envios.Zona = c.Zona
-- INNER JOIN carrier ca
-- ON ca.CarrierID = c.CarrierID
where Mes = 1;


SELECT case when mes = 1 then 'ENERO'
 when mes = 1 then 'ENERO'
			else ''
end as mes, ca.CarrierID, ca.name as [nombre], SUM(c.costo * ce.Cantidad_de_envios) as "Costo", SUM(cantidad_de_envios) as "Cantidad de Envios" from cantidad_de_envios ce
inner JOIN costos c
ON ce.Zona = c.Zona
inner join carrier ca
ON ca.CarrierID = c.CarrierID
where Mes = '1'
group by ca.CarrierID, mes, ca.name;



--select * from costos c with(nolock)

--los carrierID todos son 1
--update

--inner join carrier ca with(nolock)
--on ca.CarrierID = c.CarrierID


--select * from costos;