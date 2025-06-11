from database import criar_banco
from instituicao import verificar_instituicao, inserir_instituicao
from reservas import criar_reserva, listar_reservas

def main():
    criar_banco()

    print("=== Bem-vindo ao ITtrack ===")
    nome_inst = input("Nome da instituição: ").strip()

    id_inst = verificar_instituicao(nome_inst)

    if not id_inst:
        print("Instituição não encontrada.")
        cep = input("Digite o CEP da nova instituição (deve já existir no banco): ")
        id_inst = inserir_instituicao(nome_inst, cep)
        print("Instituição cadastrada com sucesso!")

    print(f"\nSistema ativo para a instituição: {nome_inst} (ID: {id_inst})")

    while True:
        print("\n--- Menu da Instituição ---")
        print("1. Cadastrar dispositivo e criar reserva")
        print("2. Listar reservas (formato matriz)")
        print("0. Sair")
        op = int(input("Escolha: "))

        if op == 1:
            criar_reserva(id_inst)
        elif op == 2:
            listar_reservas()
        elif op == 0:
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
