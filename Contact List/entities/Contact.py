import mysql.connector
from docutils.nodes import contact

mydb = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='python_mysql')


class Contact:

    # def __init__(self, id,first_name,last_name,number,address):
    #     self.id = id
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.number = number
    #     self.address = number

    def add_new_contact(self, user_id:int,first_name:str, last_name:str, number:str, address:str):
        cursor = mydb.cursor()
        cursor.execute(f"INSERT INTO contacts (user_id, first_name, last_name, number, address) VALUES ('{user_id}','{first_name}', '{last_name}','{number}', '{address}')")
        mydb.commit()

        # cursor.execute(f"SELECT * FROM contacts WHERE idcontacts = {cursor.lastrowid}")
        # rows = cursor.fetchall()
        #
        # # Display the results
        # for row in rows:
        #     user_id, username = row
        #     print(f"The new user has id : {user_id} - and full name : {username}")

        cursor.close()
        return None

    def update_contact(self, id, first_name, last_name, number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = number

    def get_contact(self, id, first_name, last_name, number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = number

    def delete_contact(self, id, first_name, last_name, number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = number

    def get_contact_list_owner(self, id, first_name, last_name, number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = number


contact = Contact()
contact.add_new_contact(1,'T.','Ol.','123445','Foo Bar')