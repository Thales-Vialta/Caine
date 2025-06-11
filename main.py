from database import criar_banco
from dispositivos import cadastrar_dispositivo, listar_dispositivos, atualizar_dispositivo, excluir_dispositivo
from reservas import criar_reserva, listar_reservas

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar dispositivo")
        print("2. Listar dispositivos")
        print("3. Atualizar dispositivo")
        print("4. Excluir dispositivo")
        print("5. Criar reserva")
        print("6. Listar reservas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_dispositivo()
        elif opcao == "2":
            listar_dispositivos()
        elif opcao == "3":
            atualizar_dispositivo()
        elif opcao == "4":
            excluir_dispositivo()
        elif opcao == "5":
            criar_reserva()
        elif opcao == "6":
            listar_reservas()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    criar_banco()
    menu_principal()
