from database import criar_banco
from instituicao import verificar_instituicao, inserir_instituicao
from dispositivos import cadastrar_dispositivos, listar_dispositivos, atualizar_status, excluir_dispositivo
from reserva import criar_reserva, listar_reservas

def menu_dispositivos():
    while True:
        print("\n--- Menu de Dispositivos ---")
        print("1. Cadastrar dispositivos (em série)")
        print("2. Listar dispositivos")
        print("3. Atualizar status")
        print("4. Excluir dispositivos")
        print("0. Voltar")
        op = input("Escolha: ").strip()

        if op == "1":
            cadastrar_dispositivos()
        elif op == "2":
            listar_dispositivos()
        elif op == "3":
            atualizar_status()
        elif op == "4":
            excluir_dispositivo()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def menu_reservas(id_inst):
    while True:
        print("\n--- Menu de Reservas ---")
        print("1. Criar reserva")
        print("2. Listar reservas")
        print("0. Voltar")
        op = input("Escolha: ").strip()

        if op == "1":
            criar_reserva(id_inst)
        elif op == "2":
            listar_reservas()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

def main():
    criar_banco()
    print("=== Bem-vindo ao ITtrack ===")
    nome = input("Nome da instituição: ").strip()
    id_inst = verificar_instituicao(nome)

    if not id_inst:
        print("Instituição não encontrada.")
        cep = input("Digite o CEP da nova instituição (deve já existir no banco): ")
        id_inst = inserir_instituicao(nome, cep)
        print("Instituição cadastrada com sucesso!")

    print(f"\nSistema ativo para a instituição: {nome} (ID: {id_inst})")

    while True:
        print("\n=== Menu Principal ===")
        print("A. Menu de Dispositivos")
        print("B. Menu de Reservas")
        print("C. Sair")
        escolha = input("Escolha: ").strip().upper()

        if escolha == "A":
            menu_dispositivos()
        elif escolha == "B":
            menu_reservas(id_inst)
        elif escolha == "C":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
