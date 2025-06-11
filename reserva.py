from database import conectar

def criar_reserva(id_instituicao):
    con = conectar()
    cursor = con.cursor()
    

    cursor.execute("SELECT ID_dispositivos, Marca, Modelo FROM dispositivos WHERE status = 1")
    ativos = cursor.fetchall()

    if not ativos:
        print("Nenhum dispositivo disponível para reserva.")
        con.close()
        return

    print("\n=== DISPOSITIVOS DISPONÍVEIS ===")
    for d in ativos:
        print(f"ID: {d[0]} | Marca: {d[1]} | Modelo: {d[2]}")

    try:
        id_dispositivo = int(input("Digite o ID do dispositivo a ser reservado: "))
    except ValueError:
        print("ID inválido.")
        con.close()
        return

    # Verifica se o ID é válido e está ativo
    cursor.execute("SELECT * FROM dispositivos WHERE ID_dispositivos = ? AND status = 1", (id_dispositivo,))
    if not cursor.fetchone():
        print("Dispositivo inválido ou já reservado.")
        con.close()
        return

    # Insere reserva e atualiza status
    cursor.execute("INSERT INTO reserva (ID_dispositivos) VALUES (?)", (id_dispositivo,))
    cursor.execute("UPDATE dispositivos SET status = 0 WHERE ID_dispositivos = ?", (id_dispositivo,))

    con.commit()
    con.close()
    print(f"Reserva criada com sucesso para o dispositivo ID {id_dispositivo}.")

def listar_reservas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT r.ID_reserva, r.ID_dispositivos, d.Marca, d.Modelo, d.status
        FROM reserva r
        JOIN dispositivos d ON r.ID_dispositivos = d.ID_dispositivos
    """)
    reservas = cursor.fetchall()
    con.close()

    matriz = []
    for r in reservas:
        status_str = "Ativo" if r[4] else "Inativo"
        matriz.append([r[0], r[1], r[2], r[3], status_str])

    print("\n=== RESERVAS (Formato Matriz) ===")
    for linha in matriz:
        print(linha)
