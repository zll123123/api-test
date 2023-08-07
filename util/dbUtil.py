import pymysql


class MySQLConnector:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query):
        if not self.conn:
            raise Exception("Database connection is not established.")

        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        return rows
