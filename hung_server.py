from flask import Flask, request
from PIL import Image
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    try:
        # Lấy dữ liệu hình ảnh từ yêu cầu POST
        image_data = request.data
        image_file = request.files['image']
        # Lưu ảnh vào thư mục tùy chọn
        image_file.save('/home/ducb/Local-Git-Repos/Backend-contents-generation/image.png')
        # Trả về phản hồi thành công
        return 'Siuuuuu', 200
    except Exception as e:
        # Xử lý lỗi nếu có
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
