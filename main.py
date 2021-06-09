from configuration import DB_PASSWORD, DB_PORT, DB_USER
from configuration import *
from dbconnection import Connection
import preprocessing

def connect_db():
    con = Connection(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)
    return con.connect()

if __name__ == "__main__":
    con = connect_db()
    cur = con.cursor()
    preprocessing.remover_espacios(cur)
    preprocessing.remover_acentos(cur)
    preprocessing.remover_numeracion(cur)
    preprocessing.remover_vinetas(cur)
    preprocessing.listar(cur)
    print(cur.fetchall())
    con.commit()
    con.close()