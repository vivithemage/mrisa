import requests, json

url = "http://localhost:5000/search"

data = {
    "image_url":"http://via.placeholder.com/350x150.png",
    "resized_images":False # Or true
}


headers = {'Content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(data))

#r.json to get the response as json
print(r.json())
