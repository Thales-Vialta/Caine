from database import conectar
from dispositivos import cadastrar_dispositivos

def criar_reserva(id_instituicao, id_dispositivo):
    print("Vamos cadastrar um dispositivo para reserva.")
    id_dispositivo = cadastrar_dispositivos()

    con = conectar()
    cursor = con.cursor()
    cursor.execute(
        "INSERT INTO reserva (ID_dispositivos) VALUES (?)",
        (id_dispositivo,)
    )
    con.commit()
    con.close()
    print(f"Reserva criada para a instituição ID {id_instituicao}.")

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
