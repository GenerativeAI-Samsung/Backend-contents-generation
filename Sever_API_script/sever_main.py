import subprocess
import threading
import requests
from flask import Flask,Response, request, send_file, render_template
from PIL import Image
from io import BytesIO
import mysql.connector
from mysql.connector import Error
import os
import json
import cv2
from PIL import Image
import io
from pix2tex.cli import LatexOCR
import replicate
import os
os.environ['REPLICATE_API_TOKEN'] = 'r8_UQIrfPj3KuUBklcProhoTkVzlQmKggD0itmUp'
def run_command(object_path):
    command = "blender --background ./virtual_studio/virtual_studio.blend --python ./scripts/main.py -- -fbx_file "
    command = command + object_path
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(process.stdout)

app = Flask(__name__)
@app.route('/video')
def video():
    video_path = 'output/dog_video.mp4'
    return send_file(video_path, mimetype='video/mp4')

@app.route('/get_video', methods=['POST'])
def get_image():
    # Get the name from the query parameters
    # name = request.args.get('name')

    # Fetch the image based on the name (replace with your own logic)
    # image_path = get_image(name)
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
    video_path = '../output/girl.mp4'
    return send_file(video_path, mimetype='video/mp4')
    # return send_file('/output/rendered.png0001-0105.mkv', mimetype='video/x-matroska')

@app.route('/api/json', methods=['POST'])
def handle_json():
    data = request.get_json()  # Retrieve JSON data from the request
    # Process the JSON data and generate the video
    # ...
    # Return the video as a response or its URL
    # Convert JSON object to string
    name = data['objects_list'][0]['name']
    json_str = json.dumps(data)
    # Print the JSON string
    print(json_str)
    # return jsonify({"name": name})

    image_path = get_image(name)
    # thread = threading.Thread(target=run_command, args=(image_path,))
    # thread.start()

    # video_path = '../output/1.mp4'
    # return send_file(video_path, mimetype='video/mp4')
    # thread.join()
    run_command(image_path)
    # path = "../output/"+name+".mkv"
    path = "../output/output.mkv"
    return send_file(path, mimetype='video/x-matroska')

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
@app.route('/latex_ocr', methods=['POST'])

def process_image():

    try:

        # Lấy dữ liệu hình ảnh từ yêu cầu POST

        image_data = request.data

        print(type(image_data))

        save_byte_image(image_data, '../output/image.png')
        image = cv2.imread('../output/image.png')
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        _, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blurred_threshold_image = cv2.GaussianBlur(threshold_image, (25, 25), 0)
        cv2.imwrite('../output/output_image2.jpg', blurred_threshold_image)
        model = LatexOCR()
        latex_ocr = model(Image.open('../output/output_image2.jpg'))
        print(latex_ocr)

        return latex_ocr, 200

    except Exception as e:

        # Xử lý lỗi nếu có

        return str(e), 500

@app.route('/image_context', methods=['POST'])
def get_image_context():
    image_data = request.data
    print(type(image_data))

    save_byte_image(image_data, 'output/khai.png')
    output = replicate.run( r"methexis-inc/img2prompt:50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5",input={"image": open(r"output/khai.png", "rb")})
    print(type(output))
    return str(output)

def save_byte_image(byte_data, file_path):

    # Create a BytesIO object from the byte array

    byte_stream = io.BytesIO(byte_data)

    # Open the image using PIL

    image = Image.open(byte_stream)
    

    # Save the image to the specified file path

    image.save(file_path)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
