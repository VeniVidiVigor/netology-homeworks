import psycopg2




def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS clients")
        cur.execute(
            "CREATE TABLE clients("
            "client_id SERIAL PRIMARY KEY, "
            "first_name VARCHAR(255) NOT NULL, "
            "last_name VARCHAR(255) NOT NULL, "
            "email VARCHAR(255) UNIQUE,"
            "phones INTEGER[]);")


def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO clients(first_name, last_name, email, phones) VALUES(%s, %s, %s, %s)",
            (first_name, last_name, email, phones)
        )
    pass


def add_phone(conn, client_id, phone):
    pass


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    pass


def delete_phone(conn, client_id, phone):
    pass


def delete_client(conn, client_id):
    pass


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(database="clients_db", user="postgres", password="Love638724") as conn:
    create_db(conn)
    add_client(conn, 'Kirill', 'Viazikov', 'VeniViga@mail.ru')
    pass  # вызывайте функции здесь
conn.close()
