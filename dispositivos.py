from database import conectar

def cadastrar_dispositivos():
    print("+==== Cadastro de Dispositivos em Série ====+")
    ids_dispositivos = []

    while True:
        marca = input("Marca: ").strip().upper()
        modelo = input("Modelo: ").strip()
        try:
            quantidade = int(input("Quantidade a cadastrar: "))
        except ValueError:
            print("Quantidade inválida! Tente novamente.")
            continue

        con = conectar()
        cursor = con.cursor()

        for i in range(quantidade):
            cursor.execute(
                "INSERT INTO dispositivos (Marca, Modelo, status) VALUES (?, ?, ?)",
                (marca, modelo, 1)  # status 1 = Ativo por padrão
            )
            ids_dispositivos.append(cursor.lastrowid)
            print(f"Dispositivo {i + 1} cadastrado com sucesso (ID: {cursor.lastrowid})!")

        con.commit()
        con.close()

        continuar = input("Deseja cadastrar mais dispositivos? (s/n): ").strip().lower()
        if continuar != 's':
            break

    return ids_dispositivos

def listar_dispositivos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dispositivos")
    rows = cursor.fetchall()
    con.close()

    matriz = []
    for row in rows:
        status_str = "Ativo" if row[3] else "Inativo"
        matriz.append([row[0], row[1], row[2], status_str])

    print("\n=== DISPOSITIVOS (Formato Matriz) ===")
    for linha in matriz:
        print(linha)

def atualizar_status():
    listar_dispositivos()
    try:
        id_disp = int(input("Digite o ID do dispositivo para atualizar status: "))
        novo_status = input("Novo status (ativo/inativo): ").strip().lower() == "ativo"
    except ValueError:
        print("Entrada inválida!")
        return

    con = conectar()
    cursor = con.cursor()
    cursor.execute("UPDATE dispositivos SET status = ? WHERE ID_dispositivos = ?", (int(novo_status), id_disp))
    con.commit()
    con.close()
    print("Status atualizado com sucesso!")

def excluir_dispositivo():
    listar_dispositivos()
    try:
        id_disp = int(input("Digite o ID do dispositivo que deseja excluir: "))
    except ValueError:
        print("ID inválido!")
        return

    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM dispositivos WHERE ID_dispositivos = ?", (id_disp,))
    con.commit()
    con.close()
    print("Dispositivo excluído com sucesso!")
