from database import conectar

def verificar_instituicao(nome):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id_instituicao FROM instituicao WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    con.close()
    return resultado[0] if resultado else None

def inserir_instituicao(nome, cep):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO instituicao (nome, CEP) VALUES (?, ?)", (nome, cep))
    con.commit()
    id_inst = cursor.lastrowid
    con.close()
    return id_inst
