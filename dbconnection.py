import psycopg2

class Connection:
    def __init__(self, dbname="postgres", host="localhost", port="5432", user=None, password=None):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        con = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        return con

    def close(self):
        self.con.close()