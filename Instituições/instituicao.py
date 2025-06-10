from DB.database import conectar, criar_banco
def inserir_instituicao(id_instituicao, nome, cep): 
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO instituicao (id_instituicao, nome, CEP) VALUES (?, ?, ?)",
        (id_instituicao, nome, cep)
    )
    con.commit()
    con.close()

criar_banco()

id_instituicao = input("Digite o ID da instituição: ")
nome = input("Digite o nome da instituição: ")
cep = input("Digite o CEP da instituição (deve existir na tabela endereco): ")
inserir_instituicao(id_instituicao, nome, cep)
