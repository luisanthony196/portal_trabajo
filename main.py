from configuration import DB_PASSWORD, DB_PORT, DB_USER
from configuration import *
from dbconnection import Connection
import preprocessing

def connect_db():
    con = Connection(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)
    return con.connect()

def limpiar_detalles(cur):
    preprocessing.remover_espacios(cur)
    preprocessing.remover_acentos(cur)
    preprocessing.remover_numeracion(cur)
    preprocessing.remover_vinetas(cur)


if __name__ == "__main__":
    con = connect_db()
    cur = con.cursor()
    # Operacion para limiar los datos
    limpiar_detalles(cur)
    # Llenar las tuplas modificadas con el nombre del grupo
    preprocessing.agregar_equipo(cur)
    # Listamos en la consola los datos trabajados
    preprocessing.listar(cur)
    print(cur.fetchall())
    con.commit()
    con.close()
    print("Ejecucion terminada")