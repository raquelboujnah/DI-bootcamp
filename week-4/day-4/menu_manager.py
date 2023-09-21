import psycopg2
from menu_items import MenuItems

DB_NAME = "exercises-XP-day4"
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

class MenuManager:
    
    def __init__(self, name):
        self.name = name
        self.table_name = "menu_items"
        
    def get_by_name(self):
        try:
            query = f'''
                select * from {self.table_name} where name_item = '{self.name}'
            '''
            cursor.execute(query)
            output = cursor.fetchall()
            print(output)
        except Exception as e:
            print(f"{e} The name of the item you search is not in our menu")
            
        

    @staticmethod
    def all_items():
        query = f'''
            select * from menu_items
        ''' 
        cursor.execute(query)
        output = cursor.fetchall()
        print(output)
        
item2 = MenuManager('pizza')
item2.get_by_name()
item2.all_items()
        
        