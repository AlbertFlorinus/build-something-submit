import os
import logging
from psycopg2.pool import SimpleConnectionPool
import psycopg2
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv(".env")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LocalConnectionPool:
    def __init__(self):
        self.pool = SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=5432
        )
        logging.info("Local database connection pool initialized successfully.")

    @contextmanager
    def get_connection(self):
        conn = self.pool.getconn()
        try:
            yield conn
        finally:
            self.pool.putconn(conn)

    def execute_query(self, query):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(query)
                except psycopg2.Error as e:
                    logging.error(f"Error executing query: {e}")
                    conn.rollback()
                    raise
                conn.commit()

    def read_query(self, query):
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows

    def close(self):
        self.pool.closeall()
        logging.info("All local database connections closed.")