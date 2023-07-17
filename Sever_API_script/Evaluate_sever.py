import requests
import json

# JSON data to send
data = {
  "objects_list": [
    {
      "name": "dog",
      "action": "move up",
      "timing": "first"
    },
    {
      "name": "cat",
      "action": "jump",
      "timing": "then"
    },
    {
      "name": "apple",
      "action": "roll",
      "timing": "final"
    }
  ]
}


# Convert JSON data to a string
json_data = json.dumps(data)

# Set the headers for the request
headers = {'Content-Type': 'application/json'}

# Make the POST request to the server
response = requests.post('http://localhost:5000/api/json', data=json_data, headers=headers)

# Check the response status code
if response.status_code == 200:
    video_content = response.content

    # Save the video content to a file
    with open('video.mp4', 'wb') as f:
        f.write(video_content)
    print("true")
    # ...
else:
    # Handle the error
    print("error")
