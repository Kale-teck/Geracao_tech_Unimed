create database penultimo;
show databases;
use penultimo;
show tables;
create table fornecedor (
	idfornecedor int primary key auto_increment not null unique,
    razao_social varchar(45) not null,
    cnpj varchar(30) unique not null);

drop table fornecedor;
show tables;
desc fornecedor;

CREATE TABLE produto (
    idproduto INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
    categoria VARCHAR(30) NOT NULL,
    descricao VARCHAR(60) NOT NULL,
    valor float4
);
show tables;
desc produto;
CREATE TABLE pedido (
    idpedido INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
    valor float8 NOT NULL,
    descricao VARCHAR(60) NOT NULL,
    endereco varchar(45)
);
show tables;
create table estoque (
	idestoque int primary key auto_increment not null unique,
    local_estoque varchar(45));
show tables;
create table produto_has_fornecedor (
	idproduto int,
    idfornecedor int,
    foreign key (idproduto) references produto(idproduto),
    foreign key (idfornecedor) references fornecedor(idfornecedor));
show tables;

create table pedido_has_produto (
		idpedido int,
        idproduto int,
        foreign key (idpedido) references pedido(idpedido),
        foreign key (idproduto) references produto(idproduto));

show tables;

create table terceiro_vendedor (
	idterceiro_vendedor int primary key not null unique auto_increment,
    razao_social varchar(45) not null,
    local_terceiro_vendedor varchar(45));

create table produto_has_estoque (
		idestoque int,
        idproduto int,
        foreign key (idestoque) references estoque(idestoque),
        foreign key (idproduto) references produto(idproduto));

create table terceiro_vendedor_has_produto (
		idproduto int,
        idterceiro_vendedor int,
        foreign key (idproduto) references produto(idproduto),
        foreign key (idterceiro_vendedor) references terceiro_vendedor(idterceiro_vendedor));
show tables;

create table clientes (
	idclientes int primary key unique not null auto_increment,
    nome varchar(45) not null,
    sexo enum('m', 'f', 'outro'),
    cpf varchar(20),
    endereco varchar(60));

create table clientes_has_pedido (
	idclientes int,
    idpedido int,
    foreign key (idclientes) references clientes(idclientes),
    foreign key (idpedido) references pedido(idpedido));

show tables;
desc clientes;

insert into clientes (nome, sexo, cpf, endereco)
	values ('Maria', 'f', 74659021, 'rua da uva, 235 país das Maravilhas');

insert into clientes (nome, sexo, cpf, endereco)
	values ('João', 'outro', 94947462, 'travessa Caiçara, 502 cidade das Almas'),
			('Widsney', 'm', 7777777, 'Maguesia Tumbs, centro, 1001 Rua Formiga'),
            ('Quequé', 'f', 000020, 'tudo posso naquele que me fortalece 302');

select * from clientes;

show tables;

desc produto;

insert into produto (categoria, descricao, valor)
	values ('higiene', 'sabonete íntimo', 0.50),
			('doce', 'bolacha recheada', 2.50),
            ('construção', 'tinta 30L', 25.99);
            
            
desc fornecedor;

insert into fornecedor (razao_social, cnpj) values
	('Limpa e CIA', 0800765344),
    ('Amor de Quê', 1001696969),
    ('Adossica meu Amor', 77777777);

insert into terceiro_vendedor (razao_social, local_terceiro_vendedor) values
	('Quero Mais', 'Paraguai'),
    ('Foi Ali', 'Calçada'),
    ('limpa lixo', 'EUA');
    

desc terceiro_vendedor;

show tables;

desc clientes;

select * from clientes;

show tables;

desc estoque;

select * from estoque;

alter table estoque add column quantidade int;

desc estoque;

insert into estoque (local_estoque, quantidade) values
	('Indiana', 455),
    ('Penépoles', 1955),
    ('São Domingos', 2229);
    
desc estoque;

select * from estoque;

show tables;

select * from produto_has_estoque;

select * from estoque, produto;

select * from clientes where nome like "%a%";

select * from clientes;


show tables;
desc produto;

select avg(valor) from produto;