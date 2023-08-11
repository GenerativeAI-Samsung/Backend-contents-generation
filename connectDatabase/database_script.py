import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
                                         database='Lib',  #thay đổi tên database tại đây
                                         user='debian-sys-maint',   #thay đổi username tai đây
                                         password='DiDcXj9zsaHghNd5') #thay đổi password tai đây
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
    cursor = connection.cursor()

def add_row(conn, id, name,object_path,description,table_name='Primitive3DObjects'):
    cursor = conn.cursor()
    query = "INSERT INTO "+table_name+"(Name, Object_path,Description)"+" VALUES"+" (" + "'"+name +"'"+ "," +"'" +object_path+"'"+","+"'"+description+"'"+");"
    print(query)
    cursor.execute(query)
    # Commit the changes to the database
    conn.commit()
    # Close the cursor and connection when you're done
    cursor.close()
    return 0
# def delete_row(conn, id, name,object_path,description,table_name='Primitive3DObjects'):
def delete_row(conn,name,table_name='Primitive3DObjects'):
    cursor = conn.cursor()
    query = "DELETE FROM "+table_name+" WHERE Name = "+"'"+ name +"'" + ";"
    print(query)
    cursor.execute(query)
    # Commit the changes to the database
    conn.commit()
    # Close the cursor and connection when you're done
    cursor.close()
    return 0
def update_row(conn, id, name,object_path,description,table_name='Primitive3DObjects'):
    cursor = conn.cursor()
    query = "UPDATE "+table_name+" SET Object_path = "+ "'" + object_path + "'" + " WHERE Name = " + "'" + name + "';"
    print(query)
    cursor.execute(query)
    # Commit the changes to the database
    conn.commit()
    # Close the cursor and connection when you're done
    cursor.close()
    return 0
def query_object_path(conn, id, name,table_name='Primitive3DObjects'):
    cursor = conn.cursor()
    query = "SELECT Object_path FROM "+table_name+" WHERE name = " +"'"+ name +"';"
    print(query)
    cursor.execute(query)
    row = cursor.fetchone()[0]
    print(row)
    # Commit the changes to the database
    conn.commit()
    # Close the cursor and connection when you're done
    cursor.close()
    return 0

# update_row(connection,0,"lion","~/Object-3D/lion/source/lion.glb","object 3d of a lion")
# delete_row(connection,"Fan")
# add_row(connection,0,"samsung phone","~/Object-3D/samsung-galaxy-s21-violet/source/Samsung Galaxy S21.fbx","object 3d of samsung phone")
# query_object_path(connection,0,"lion")
