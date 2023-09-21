import psycopg2

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
    
class MenuItems:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.table_name = 'menu_items'
        
    def delete(self):
        query = f'''
            select id from {self.table_name} where name_item = '{self.name}'
        '''
        cursor.execute(query)
        output = cursor.fetchall()[0][0]
        query = f'''
            delete from {self.table_name} where id = {output}
        '''
        cursor.execute(query)
        connection.commit()
        
        
    def save(self):
        query = f'''
            insert into {self.table_name}(name_item, price_item)
            values
            ('{self.name}', '{self.price}')
        '''
        cursor.execute(query)
        connection.commit() 
        
               
    def update(self, new_name, new_price):
        query = f'''
            update {self.table_name}
            set name_item = '{new_name}', price_item = '{new_price}'
            where name_item = '{self.name}'
        '''
        cursor.execute(query)
        connection.commit() 
        
item = MenuItems('pizza', 7)  
# item.save()       
# item.delete()
# item.update('vegie pizza', 8)
        