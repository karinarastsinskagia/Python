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

def get_users_and_contacts():
    cursor = mydb.cursor()
    cursor.execute(f"SELECT users.username, contacts.first_name, contacts.number FROM users JOIN contacts ON users.idusers = contacts.user_id")
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        username,first_name,number = row
        print(f"User Name : {username} - Contact Name : {first_name} - Number : {number}")
    # Close the cursor and connection
    cursor.close()

    return None


def get_a_user(user_id):
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

def create_new_user(name: str):
    cursor = mydb.cursor()
    cursor.execute(f"INSERT INTO users (username) VALUES ('{name}')")
    mydb.commit()

    cursor.execute(f"SELECT * FROM users WHERE idusers = {cursor.lastrowid}")
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        user_id, username = row
        print(f"The new user has id : {user_id} - and full name : {username}")

    cursor.close()
    return None

def update_username(userid:int, name: str):

    cursor = mydb.cursor()
    cursor.execute(f"UPDATE users SET username= '{name}' WHERE idusers = {userid}")
    mydb.commit()
    cursor.close()

    return None

def delete_user(userid:int):

    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM users WHERE idusers = {userid}")
    mydb.commit()
    cursor.close()

    return None

def get_users_contact_list(user_id:int):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT first_name,last_name,number,address FROM contacts WHERE user_id = {user_id}")
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        first_name,last_name,number,address = row
        print(f"First Name : {first_name} - Last Name : {last_name} - Address : {address} - Number : {number}")
    # Close the cursor and connection
    cursor.close()

    return None


######### Methods execution (examples) ##########

# get_all()
#create_new_user("Kathrin Hill")
#get_a_user(1)
#get_a_user(45)
#create_new_user("George Orwell")
#update_username(1,"Kathrin Hilton")
# delete_user(2)
#get_users_contact_list(1)
#get_users_and_contacts()





