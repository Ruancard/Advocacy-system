create database advocacia;

\c advocacia;

create table advogados(
oab varchar(8) not null primary key,
usuario varchar(30) not null,
senha varchar(50) not null,
admin boolean default false,
cpf varchar(15) not null,
nome varchar(50) not null,
sobrenome varchar(50) not null,
nascimento date not null,
email varchar(100) not null,
tel varchar(15) not null,
estado varchar(3) not null,
cidade varchar(30) not null,
bairro varchar(30) not null,
rua varchar(30) not null,
numero int not null,
cep varchar(10) not null
);

create table clientes(
cpf varchar(15) not null primary key,
nome varchar(50) not null,
sobrenome varchar(50) not null,
nascimento date not null,
email varchar(100) not null,
tel varchar(15) not null,
estado varchar(3) not null,
cidade varchar(30) not null,
bairro varchar(30) not null,
rua varchar(30) not null,
numero int not null,
cep varchar(10) not null
);

create table processos(
numero varchar(20) not null primary key,
nome varchar(50) not null,
descricao varchar(300) not null,
observacao varchar(100),
vara varchar(15) not null,
requerente varchar(50) not null,
reu varchar(50) not null,
acusacao varchar(50) not null,
defesa varchar(50) not null,
juiz varchar(50) not null,
dt_inicio date not null,
dt_att date not null
);

insert into processos(numero, nome, descricao, observacao, vara, requerente, reu, acusacao, defesa, juiz, dt_inicio, dt_att)
values('23123131312231', 'processando o dentista', 'processo contra um destista paulista', 'o dentista não tem os dentes',
'sp', 'alan dos santos', 'osmar pereira', 'leandro torres', 'ryan guimaraes', 'uscelino cap', '2022-03-15', '2022-05-14');