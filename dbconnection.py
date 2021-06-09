import psycopg2

class Connection:
    def __init__(self, host="localhost", port="5432", user=None, password=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        con = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="prueba",
            host="localhost",
            port="5432"
        )
        return con

    def close(self):
        self.con.close()