import pycurl, json
from flask import Flask, url_for, json, request
from StringIO import StringIO
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/search', methods = ['POST'])

# first function called
def mrisa_main():
    # Detect the content type, only process if it's json, otherwise send an error
    if request.headers['Content-Type'] == 'application/json':
        client_json = json.dumps(request.json)
        client_data = json.loads(client_json)
        code = retrieve(client_data['image_url'])
        return google_image_results_parser(code)
        #return "JSON Message: " + json.dumps(request.json)
    else:
        json_error_message = "Requests need to be in json format. Please make sure the header is 'application/json' and the json is valid."
        return json_error_message

# retrieves the reverse search html for processing. This actually does the reverse image lookup
def retrieve(image_url):
    returned_code = StringIO()
    full_url = 'https://www.google.com/searchbyimage?&image_url=' + image_url
    conn = pycurl.Curl()
    conn.setopt(conn.URL, full_url)
    conn.setopt(conn.FOLLOWLOCATION, 1)
    conn.setopt(conn.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11')
    conn.setopt(conn.WRITEFUNCTION, returned_code.write)
    conn.perform()
    conn.close()
    return returned_code.getvalue()

# Parses returned code (html,js,css) and assigns to array using beautifulsoup
def google_image_results_parser(code):
    soup = BeautifulSoup(code)

    # initialize 2d array
    whole_array = {'links':[],
                   'description':[],
                   'title':[],
                   'result_qty':[]}

    # Links for all the search results
    for li in soup.findAll('li', attrs={'class':'g'}):
        sLink = li.find('a')
        whole_array['links'].append(sLink['href'])

    # Search Result Description
    for desc in soup.findAll('span', attrs={'class':'st'}):
        whole_array['description'].append(desc.get_text())

    # Search Result Title
    for title in soup.findAll('h3', attrs={'class':'r'}):
        whole_array['title'].append(title.get_text())

    # Number of results
    for result_qty in soup.findAll('div', attrs={'id':'resultStats'}):
        whole_array['result_qty'].append(result_qty.get_text())

    return build_json_return(whole_array)

def build_json_return(whole_array):
    return json.dumps(whole_array)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
