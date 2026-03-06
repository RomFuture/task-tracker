import psycopg2
import os
import dotenv


class DBConnection:
    def __init__(self):
        dotenv.load_dotenv()
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_PORT = os.getenv("DB_PORT")
    def connect_to_db(self):
        conn = psycopg2.connect(host=self.DB_HOST, dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD, port=self.DB_PORT)
        cursor = conn.cursor()
        return conn, cursor
    def close_db_connection(self, cursor, conn):
        cursor.close()
        conn.close()
