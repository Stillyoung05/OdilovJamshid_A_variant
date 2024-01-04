import psycopg2

db_config = {
    'host': 'host',
    'database': 'db_name',
    'user': 'username',
    'password': 'pswrd',
    'port': 'port',
}
connection = psycopg2.connect(**db_config)
cursor = connection.cursor()
table_name = 'exam_table'
query = """select from * """

cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()
