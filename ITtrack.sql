create table dispositivos(
    ID_dispositivos INTEGER PRIMARY key, 
    Marca varchar (30) not null, 
    Modelo varchar(50) not null,
    status boolean not null
); 
create table endereco (
    CEP varchar(9) not null PRIMARY key, 
    cidade varchar(100) not null, 
    bairro varchar(70) not null, 
    estado char(2) not null,
    numero int, 
    descricao varchar(200) not null, 
); 
CREATE TABLE instituicao(
    id_instituicao int PRIMARY KEY NOT NULL, 
    nome VARCHAR(70) not null, 
    CEP VARCHAR(9) not null, 
    FOREIGN KEY (CEP) REFERENCES endereco(CEP)
); 
CREATE TABLE reserva(
    ID_reserva INT PRIMARY KEY NOT NULL, 
    ID_dispositivos int, 
    FOREIGN KEY (ID_dispositivos) REFERENCES dispositivos(ID_dispositivos)
); 