from database import conectar

def cadastrar_dispositivo():
    marca = input("Marca do dispositivo: ")
    modelo = input("Modelo do dispositivo: ")
    status = input("Status (ativo/inativo): ").strip().lower() == "ativo"
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO dispositivos (Marca, Modelo, status) VALUES (?, ?, ?)", 
                   (marca, modelo, int(status)))
    con.commit()
    id_disp = cursor.lastrowid
    con.close()
    print("Dispositivo cadastrado com sucesso!")
    return id_disp

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
