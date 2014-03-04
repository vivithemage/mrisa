import pycurl, json
from flask import Flask, url_for, json, request

app = Flask(__name__)

@app.route('/search', methods = ['POST'])

# first function called
def mrisa_main():
    # Detect the content type, only process if it's json, otherwise send an error
    if request.headers['Content-Type'] == 'application/json':
        client_json = json.dumps(request.json)
        client_data = json.loads(client_json)
        return "JSON Message: " + json.dumps(request.json)
    else:
        json_error_message = "Requests need to be in json format. Please make sure the header is 'application/json' and the json is valid."
        return json_error_message

# retrieves the reverse search html for processing. This actually does the reverse image lookup
def retrieve(image_url):
    full_url = 'https://www.google.com/searchbyimage?&image_url=' + image_url
    c = pycurl.Curl()
    c.setopt(c.URL, image_url)
    c.setopt(c.FOLLOWLOCATION, true)
    # Need to set the useragent as an actual client rather than just curl.
    c.setopt(c.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11')
    c.perform()
    return 'bleh'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
