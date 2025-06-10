from banco import conectar,criar_banco
        
def inserir_escola(id_instituicao,nome): 
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO dispositivos (ID_dispositivos, Marca, Modelo, status) VALUES (?, ?, ?, ?)",
        (id_instituicao, nome)  
    )
    con.commit()
    con.close()
criar_banco()
inserir_escola.nome(input("Digite o nome da escola:" ));