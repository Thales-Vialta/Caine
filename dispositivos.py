from database import conectar

def cadastrar_dispositivos():
    n = int(input("Quantos dispositivos deseja cadastrar? "))
    ids_dispositivos = []

    for i in range(n):
        print(f"\n--- Cadastro do dispositivo {i+1} ---")
        marca = input("Marca do dispositivo: ")
        modelo = input("Modelo do dispositivo: ")
        status = 1 

        con = conectar()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO dispositivos (Marca, Modelo, status) VALUES (?, ?, ?)", 
            (marca, modelo, status)
        )
        con.commit()
        id_disp = cursor.lastrowid
        ids_dispositivos.append(id_disp)
        con.close()

        print(f"Dispositivo {i+1} cadastrado com sucesso (ID: {id_disp})!")

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
