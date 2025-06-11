from database import conectar
from dispositivos import listar_dispositivos

def criar_reserva():
    listar_dispositivos()
    id_disp = input("ID do dispositivo que deseja reservar: ")

    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO reserva (ID_dispositivos) VALUES (?)", (id_disp,))
    con.commit()
    con.close()
    print("Reserva criada com sucesso!")

def listar_reservas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        SELECT r.ID_reserva, d.Marca, d.Modelo
        FROM reserva r
        JOIN dispositivos d ON r.ID_dispositivos = d.ID_dispositivos
    """)
    reservas = cursor.fetchall()
    con.close()

    if reservas:
        print("\n=== Reservas ===")
        for r in reservas:
            print(f"Reserva ID: {r[0]} | Dispositivo: {r[1]} {r[2]}")
    else:
        print("Nenhuma reserva registrada.")
