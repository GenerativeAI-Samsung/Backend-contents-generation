from flask import Flask, render_template, send_file

# Create the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/video')
def video():
    video_path = 'output/dog_video.mp4'
    return send_file(video_path, mimetype='video/mp4')

@app.route('/image')
def image():
    video_path = 'output/Dog.png'
    return send_file(video_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)#, debug=True)