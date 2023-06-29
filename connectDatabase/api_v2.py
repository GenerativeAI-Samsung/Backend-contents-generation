import requests
from flask import Flask,Response, request, send_file
from PIL import Image
from io import BytesIO
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/get_image', methods=['GET'])
def get_image():
    # Get the name from the query parameters
    name = request.args.get('name')

    # Fetch the image based on the name (replace with your own logic)
    image_path = get_image(name)

    # Trả về hình ảnh như một phản hồi từ API
    return send_file(image_path, mimetype='image/jpeg')

def get_image(name):
    connection = mysql.connector.connect(host='localhost',
                                         database='Lib',
                                         user='debian-sys-maint',
                                         password='DiDcXj9zsaHghNd5')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor = connection.cursor()
        query = "SELECT image_path FROM imageObjects WHERE Name = %s"  # Replace 'your_table' and 'id' with appropriate values
        params = (name,)  # Replace 'your_id' with the actual ID value you want to retrieve

        cursor.execute(query, params)
        result = cursor.fetchone()[0]  # Assuming there is only one row and one column
        return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
