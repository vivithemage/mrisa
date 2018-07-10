import requests, json

url = "http://localhost:5000/search"

data = {
    "image_url":"http://2.bp.blogspot.com/-pZsU4tr2gS8/VnpucHNahCI/AAAAAAAAPjI/bdwQMlqzHxw/s0-Ic42/RCO001.jpg",
    "resized_images":False # Or true
}


headers = {'Content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(data))

#r.json to get the response as json
print(r.json())