import mysql.connector
mydb = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='python_mysql')


def add_new_contact(user_id:int,first_name:str, last_name:str, number:str, address:str):
    cursor = mydb.cursor()
    cursor.execute(f"INSERT INTO contacts (user_id, first_name, last_name, number, address) VALUES ('{user_id}','{first_name}', '{last_name}','{number}', '{address}')")
    mydb.commit()

    cursor.close()
    return None

def update_contact(contactid:int, args:dict):
    #  first_name:None, last_name:None, number:None, address:None
    cursor = mydb.cursor()

    query_part = []
    values = []
    for key,value in args.items():
        query_part.append(key +"= %s")
        values.append(value)

    query = f"UPDATE contacts SET {', '.join(query_part)} WHERE idcontacts = {contactid}"

    cursor.execute(query,values)
    mydb.commit()
    cursor.close()

    return None

def delete_contact(contactid:int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM contacts WHERE idcontacts = {contactid}")
    mydb.commit()
    cursor.close()

    return None

def get_contact_list_owner(contactid:int):
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT users.username FROM users JOIN contacts ON users.idusers = contacts.user_id WHERE contacts.idcontacts = {contactid}")
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        username = row
        print(f"User Name : {username} (for the given contact)")
    # Close the cursor and connection
    cursor.close()

    return None

def get_contact(contact_id:int):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT  first_name, last_name, address, number FROM contacts WHERE idcontacts = {contact_id}")
    rows = cursor.fetchall()

    if not rows:
        print("There is no Contact with the given id")
        return None

    # Display the results
    for row in rows:
        first_name, last_name, address, number = row
        print(f"First Name : {first_name} - Last Name : {last_name} - Address : {address} - Number : {number}")
    # Close the cursor and connection
    cursor.close()

    return None

######### Methods execution (examples) ##########

#add_new_contact(1,'T.','Ol.','123445','Foo Bar')
#get_contact_list_owner(1)
#delete_contact(6)

# args: dict[str, str] = {"first_name" : "K.", "last_name" : "Op.",}
# update_contact(1, args)
# args: dict[str, str] = {"number" : "89890"}
# update_contact(1, args)
# get_contact(1)