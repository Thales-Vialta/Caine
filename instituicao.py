from database import conectar, criar_banco

con = conectar()
cursor = con.cursor()

def inserir_instituicao(nome, cep): 
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO instituicao (nome, CEP) VALUES (?, ?)",
        (nome, cep)
    )
    con.commit()
    con.close()
    
criar_banco()

def cep_existe(cep):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM endereco WHERE CEP = ?", (cep,))
    resultado = cursor.fetchone()
    con.close()
    return resultado is not None

while True:
    nome = input("Digite o nome da instituição: ")
    cep = input("Digite o CEP da instituição (deve existir n tabela endereco): ")
    if cep_existe(cep): 
        inserir_instituicao(nome, cep)
        print("Instituição inserida com sucesso!")
    else: 
        print("CEP Inválido!")
    continuar = input("Deseja inserir outra instituição? (s/n): ").lower()
    if continuar != 's':
        break
