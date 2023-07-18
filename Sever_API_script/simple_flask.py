from flask import Flask, render_template, send_file, jsonify, request
import json
# Create the Flask application
app = Flask(__name__)

@app.route('/video')
def video():
    video_path = '../output/dog_video.mp4'
    return send_file(video_path, mimetype='video/mp4')

@app.route('/image')
def image():
    video_path = '../output/Dog.png'
    return send_file(video_path, mimetype='image/jpeg')

@app.route('/api/name')
def name():
    with open("Sever_API_script/flask.json", encoding="utf-8") as f: #open file flask.json on sever
        name = json.load(f)
        return jsonify({"name": name})
@app.route('/api/json', methods=['POST'])
def handle_json():
    data = request.get_json()  # Retrieve JSON data from the request
    json_str = json.dumps(data)
    # Print the JSON string
    print(json_str)
    # return jsonify({"name": name})

    # video_url = 'http://example.com/videos/video123.mp4'
    # response = {'video_url': video_url}
    # return jsonify(response)
    video_path = '../output/1.mp4'
    return send_file(video_path, mimetype='video/mp4')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
