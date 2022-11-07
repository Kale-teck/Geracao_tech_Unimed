show databases;
create database oficina;
show databases;
use oficina;
show tables;
create table cliente (
	id_cliente int not null unique auto_increment primary key,
    nome varchar(32) not null,
    cpf varchar(32) not null unique,
    endereco varchar(45) not null);
show tables;
desc cliente;
create table veiculo (
	id_veiculo int not null unique auto_increment primary key,
    marca varchar(16) not null,
    modelo varchar(16) not null unique,
    ano date not null,
    chassi varchar(90) not null,
    cliente_id_cliente int,
    foreign key (cliente_id_cliente) references cliente(id_cliente));

create table mecanico (
	id_mecanico int not null unique auto_increment primary key,
    nome varchar(32) not null,
    cpf varchar(32) not null unique,
    endereco varchar(45) not null,
    especialidade varchar(45) not null);

create table equipe (
	id_equipe int not null unique auto_increment primary key,
    nome varchar(32) not null,
    chefe varchar(32) not null,
    mecanico_id_mecanico int not null,
    setor varchar(16));

show tables;

create table ordem_servico (
	id_ordem_servico int not null unique auto_increment primary key,
    data_emissao datetime not null,
    data_conclusao date,
    status_os varchar(45) not null,
    valor float,
    equipe_id_equipe int not null,
    foreign key (equipe_id_equipe) references equipe(id_equipe));
    

create table servico (
	id_servico int not null unique auto_increment primary key,
    concerto varchar(45),
    manutencao varchar(45),
    id_ordem_servico int not null,
    id_equipe int not null,
    foreign key (id_ordem_servico) references ordem_servico(id_ordem_servico),
    foreign key (id_equipe) references equipe(id_equipe));

show tables;
desc mecanico;

create table pecas (
	id_pecas int not null unique auto_increment primary key,
    peca varchar(45),
    preco float);

create table pecas_has_servico (
	pecas_id_pecas int not null,
    servico_id_servico int not null,
    ordem_servico_id_ordem_servico int not null,
    equipe_id_equipe int not null,
    foreign key (pecas_id_pecas) references pecas(id_pecas),
    foreign key (servico_id_servico) references servico(id_servico),
    foreign key (ordem_servico_id_ordem_servico) references ordem_servico(id_ordem_servico),
    foreign key (equipe_id_equipe) references equipe(id_equipe));

-- criadas as tabelas irei inserir os dados para testes e consultas

insert into cliente (nome, cpf, endereco)
	values ('João', 94947462, 'travessa Caiçara, 502 cidade das Almas'),
			('Widsney', 7777777, 'Maguesia Tumbs, centro, 1001 Rua Formiga'),
            ('Quequé', 000020, 'tudo posso naquele que me fortalece 302'),
            ('Jackson', 111020, 'Rua do Gol quadrado, 1000');

insert into mecanico (nome, cpf, endereco, especialidade)
	values ('Zeca', 97425, 'Rua da Rezenha, 502 cidade das Almas', 'eletrica'),
			('Fuca', 899915, 'Praia do Futuro, centro, 1001 Rua Formiga', 'pintura'),
            ('Mizi', 937569, 'tudo posso naquele que me fortalece 666', 'borracharia'),
            ('Pedo', 756463, 'Rua da Onça Mansa, 14', 'retifica');

show tables;
desc equipe;

drop table mecanico;

select * from mecanico;

show tables;

desc pecas;
insert into pecas (peca, preco) values
	('parafuso', 0.25),
    ('Retrovisor', 150.99),
    ('Farol', 300),
    ('pneu 12 165/55', 200.00),
	('pneu 13 180/50', 350.00),
    ('porta celta', 2500.00),
    ('roda liga 16', 1900.99);

show tables;
desc cliente;
select * from cliente;
show tables;
select * from mecanico;
show tables;
select * from pecas;
show tables;
desc veiculo;
select * from veiculo ;
drop table veiculo;

insert into veiculo (marca, modelo, ano, chassi) values
	('VW', 'voyage', 2011-05-20, 86363);
    
insert into veiculo (cliente_id_cliente) value (1);

delete from veiculo where id_veiculo=6;

update veiculo set cliente_id_cliente=1 where id_veiculo=4;

select avg(preco) from pecas;


insert into veiculo (marca, modelo, ano, chassi) values
	('VW', 'Gol', 2015-05-00, 198374),
    ('Audi', 'A4', 2019-08-29, 978664);

select * from cliente;

update veiculo set cliente_id_cliente=4 where id_veiculo=7;
update veiculo set cliente_id_cliente=3 where id_veiculo=8;