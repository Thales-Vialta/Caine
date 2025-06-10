import sqlite3

def conectar():
    return sqlite3.connect('ITtrack.db')

def criar_banco(): 
    con = conectar()
    cursor = con.cursor()
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS dispositivos(
        ID_dispositivos INTEGER PRIMARY KEY NOT NULL, 
        Marca VARCHAR(30) NOT NULL, 
        Modelo VARCHAR(50) NOT NULL,
        status BOOLEAN NOT NULL
    ); 

    CREATE TABLE IF NOT EXISTS endereco (
        CEP VARCHAR(9) PRIMARY KEY NOT NULL, 
        cidade VARCHAR(100) NOT NULL, 
        bairro VARCHAR(70) NOT NULL, 
        estado CHAR(2) NOT NULL,
        numero INT, 
        descricao VARCHAR(200) NOT NULL
    ); 

    CREATE TABLE IF NOT EXISTS instituicao(
        id_instituicao INTEGER PRIMARY KEY NOT NULL, 
        nome VARCHAR(70) NOT NULL, 
        CEP VARCHAR(9) NOT NULL, 
        FOREIGN KEY (CEP) REFERENCES endereco(CEP)
    ); 

    CREATE TABLE IF NOT EXISTS reserva(
        ID_reserva INTEGER PRIMARY KEY NOT NULL, 
        ID_dispositivos INTEGER, 
        FOREIGN KEY (ID_dispositivos) REFERENCES dispositivos(ID_dispositivos)
    );
    ''')
    con.commit()
    con.close()


