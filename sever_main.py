import subprocess
import threading
import requests
from flask import Flask,Response, request, send_file, render_template
from PIL import Image
from io import BytesIO
import mysql.connector
from mysql.connector import Error
import os

def run_command(object_path):
    command = "blender ./virtual_studio/virtual_studio.blend --python ./scripts/load_obj.py -- -fbx_file "
    command = command + object_path
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(process.stdout)

app = Flask(__name__)
@app.route('/video')
def video():
    video_path = 'output/dog_video.mp4'
    return send_file(video_path, mimetype='video/mp4')

@app.route('/get_image', methods=['GET'])
def get_image():
    # Get the name from the query parameters
    name = request.args.get('name')

    # Fetch the image based on the name (replace with your own logic)
    # image_path = get_image(name)

    # Trả về hình ảnh như một phản hồi từ API
    # command = "blender ./virtual_studio/virtual_studio.blend --python ./scripts/load_obj.py -- -fbx_file "
    # command = command + image_path
    # print(command)
    # result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # print(result.stdout)
    # run_command(image_path)
    # thread = threading.Thread(target=run_command, args=(image_path,))
    # thread.start()
    # path = "./output/"+name+".png"
    # print(path)
    # while not (os.path.exists(path) and os.path.getsize(image_path) > 0):
    #     pass
    # print("success")
    # thread.join()
    # return render_template('video_display.html')
    # return send_file("output/Dog.png", mimetype='image/jpeg')
    video_path = 'output/dog_video.mp4'
    return send_file(video_path, mimetype='video/mp4')
    # return send_file('/output/rendered.png0001-0105.mkv', mimetype='video/x-matroska')



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
        query = "SELECT object_path FROM 3D_Object_Blender WHERE Name = %s"  # Replace 'your_table' and 'id' with appropriate values
        params = (name,)  # Replace 'your_id' with the actual ID value you want to retrieve

        cursor.execute(query, params)
        result = cursor.fetchone()[0]  # Assuming there is only one row and one column
        return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)#, debug=True)
