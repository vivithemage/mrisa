import pycurl, json
from flask import Flask, url_for, json, request

app = Flask(__name__)

@app.route('/search', methods = ['POST'])

def api_message():
    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    else:
        json_error_message = "Requests need to be in JSON format. For an example, please take a look at: http://mrisa.mage.me.uk"
        return json_error_message

def retrieve():
    with open("cat-calms-cat-chill-bro-540x405.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    encoded_string = url
    c = pycurl.Curl()
    c.setopt(c.URL, )
    #c.setopt(c.POSTFIELDS, 'encoded_image=' + encoded_string)
    c.setopt(c.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11')
    c.perform()
    return 'bleh'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
