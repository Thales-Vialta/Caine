'''Receber o CEP do usuário
— No seu formulário, interface ou função, capture o CEP digitado.
Consultar a API ViaCEP
— Use sua função buscar_endereco() para pegar os dados do CEP (cidade, bairro, estado etc.).
Verificar se o CEP já existe no banco
— Antes de inserir, consulte o banco para ver se o CEP já está na tabela endereco. Se estiver, você não precisa inserir de novo.
Se o CEP não existir:
— Use os dados retornados pela API para inserir um novo registro na tabela endereco, incluindo o CEP, cidade, bairro e estado. Você pode pedir o número e descrição diretamente ao usuário nesse momento.
Inserir a instituição ou entidade relacionada
— Com o CEP já na tabela endereco, você pode inserir os dados da instituicao ou outra tabela que use esse CEP como chave estrangeira.
Manter a integridade relacional
— Garanta que, ao inserir dados em tabelas com chave estrangeira, os valores referenciados (como o CEP) já estejam no banco — esse processo resolve isso.
Você pode colocar a inserção do endereço e da instituição em uma única função (ou módulo), que:

chama a API,

insere o endereço se for novo,

e depois insere a instituição, usando o mesmo CEP como chave estrangeira.'''

from database import conectar, criar_banco
import requests

def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return None

def inserir_endereco(cep, cidade, bairro, estado, numero, descricao):
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO endereco (CEP, cidade, bairro, estado, numero, descricao) VALUES (?, ?, ?, ?, ?, ?)",
        (cep, cidade, bairro, estado, numero, descricao)
    )
    con.commit()
    con.close()

criar_banco()

cep = input("Digite o CEP: ").strip()
endereco = buscar_endereco(cep)

if endereco and 'erro' not in endereco:
    cidade = endereco['localidade']
    bairro = endereco['bairro']
    estado = endereco['uf']

    print(f"Endereço encontrado: {bairro}, {cidade} - {estado}")

    numero = input("Digite o número: ").strip()
    descricao = input("Digite a descrição (opcional): ").strip()

    inserir_endereco(cep, cidade, bairro, estado, numero, descricao)
    print("Endereço salvo com sucesso!")
else:
    print("CEP inválido ou não encontrado.")
