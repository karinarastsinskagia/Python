import Contact
import mysql.connector

mydb = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='python_mysql')


def get_all():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        user_id, username = row
        print(f"id : {user_id} - full name : {username}")
    # Close the cursor and connection
    cursor.close()

    return None


class User:

    id: int
    name: str
    contact_list: Contact

    # def __init__(self,id:int,name:str):
    #     self.id = id
    #     self.name = name

    def get_a_user(self, user_id):
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM users WHERE idusers = {user_id}")
        rows = cursor.fetchall()

        if not rows:
            print("There is no User with the given id")
            return None

        # Display the results
        for row in rows:
            user_id, username = row
            print(f"id : {user_id} - full name : {username}")
        # Close the cursor and connection
        cursor.close()

        return None

    def create_new_user(self,name: str):
        cursor = mydb.cursor()
        cursor.execute(f"INSERT INTO users (username) VALUES ('{name}')")
        cursor.execute(f"SELECT * FROM users WHERE idusers = {cursor.lastrowid}")
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            user_id, username = row
            print(f"The new user has id : {user_id} - and full name : {username}")

        cursor.close()
        return None

# def update_username(name: str):
#     return None

# def delete_user(name: str):
#     return None

# def get_users_contact_list():
#     return User.contact_list

######### Methods execution ##########
get_all()

user = User()
user.get_a_user(1)
user.get_a_user(45)

user.create_new_user("Kathrin Hill")



