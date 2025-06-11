'''preciso criar um criador de arquivo onde eu armazene num arquivo, nome, tipo, status'''
from database import conectar

def cadastrar_dispositivo():
    marca = input("Marca do dispositivo: ")
    modelo = input("Modelo do dispositivo: ")
    status = input("Status (ativo/inativo): ").strip().lower() == "ativo"
    
    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO dispositivos (Marca, Modelo, status) VALUES (?, ?, ?)",
        (marca, modelo, int(status))
    )
    con.commit()
    con.close()
    print("Dispositivo cadastrado com sucesso!")

def listar_dispositivos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM dispositivos")
    rows = cursor.fetchall()
    con.close()

    if rows:
        print("\n=== Dispositivos ===")
        for row in rows:
            status = "Ativo" if row[3] else "Inativo"
            print(f"ID: {row[0]} | Marca: {row[1]} | Modelo: {row[2]} | Status: {status}")
    else:
        print("Nenhum dispositivo cadastrado.")

def atualizar_dispositivo():
    listar_dispositivos()
    id_disp = input("ID do dispositivo que deseja atualizar: ")
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    status = input("Status (ativo/inativo): ").strip().lower() == "ativo"

    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        UPDATE dispositivos 
        SET Marca = ?, Modelo = ?, status = ?
        WHERE ID_dispositivos = ?""",
        (marca, modelo, int(status), id_disp)
    )
    con.commit()
    con.close()
    print("Dispositivo atualizado com sucesso!")

def excluir_dispositivo():
    listar_dispositivos()
    id_disp = input("ID do dispositivo que deseja excluir: ")

    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM dispositivos WHERE ID_dispositivos = ?", (id_disp,))
    con.commit()
    con.close()
    print("Dispositivo excluído com sucesso!")
