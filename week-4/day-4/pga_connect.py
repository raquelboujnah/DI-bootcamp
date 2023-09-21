import psycopg2

DB_NAME = "dvdrental"
USER = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
PORT = "5432"

try:
    connection = psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
except Exception as e:
    print(f"Error: {e}")

cursor = connection.cursor()

def create_table(table_name: str):
    
    query = f'''
    create table {table_name}(
        id serial primary key,
        num integer not null
    );
    '''
    cursor.execute(query)
    connection.commit()
    
def insert_into_table(table_name: str, num_value: int):
    query = f'''
    insert into {table_name}(num)
    values
    ({num_value})
    '''
    cursor.execute(query)
    connection.commit()
    
    
# create_table("new_table2")    
# insert_into_table("new_table2", 100)
# insert_into_table("new_table2", 1000)

table_name = "new_table2"
query = f'''
select * from {table_name}
'''

cursor.execute(query)
output = cursor.fetchall()

# print(output)

connection.close()


