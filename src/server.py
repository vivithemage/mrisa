import argparse
import pycurl
import json
from flask import Flask, url_for, json, request
python3 = False
try:
    from StringIO import StringIO
except ImportError:
    python3 = True
    import io as bytesIOModule
from bs4 import BeautifulSoup
if python3:
    import certifi

SEARCH_URL = 'https://www.google.com/searchbyimage?&image_url='

app = Flask(__name__)

@app.route('/search', methods = ['POST'])
def search():
    if request.headers['Content-Type'] != 'application/json':
        return "Requests must be in JSON format. Please make sure the header is 'application/json' and the JSON is valid."

    client_json = json.dumps(request.json)
    client_data = json.loads(client_json)
    code = doImageSearch(client_data['image_url'])
    return parseResults(code)

def doImageSearch(image_url):
    """Perform the image search and return the HTML page response."""

    if python3:
        returned_code = bytesIOModule.BytesIO()
    else:
        returned_code = StringIO()
    full_url = SEARCH_URL + image_url

    if app.debug:
        print('POST: ' + full_url)

    conn = pycurl.Curl()
    if python3:
        conn.setopt(conn.CAINFO, certifi.where())
    conn.setopt(conn.URL, str(full_url))
    conn.setopt(conn.FOLLOWLOCATION, 1)
    conn.setopt(conn.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11')
    conn.setopt(conn.WRITEFUNCTION, returned_code.write)
    conn.perform()
    conn.close()
    if python3:
        return returned_code.getvalue().decode('UTF-8')
    else:
        return returned_code.getvalue()

def parseResults(code):
    """Parse/Scrape the HTML code for the info we want."""

    soup = BeautifulSoup(code, 'html.parser')

    results = {
        'links': [],
        'descriptions': [],
        'titles': [],
        'similar_images': [],
        'best_guess': ''
    }

    for div in soup.findAll('div', attrs={'class':'rc'}):
        sLink = div.find('a')
        results['links'].append(sLink['href'])

    for desc in soup.findAll('span', attrs={'class':'st'}):
        results['descriptions'].append(desc.get_text())

    for title in soup.findAll('h3', attrs={'class':'r'}):
        results['titles'].append(title.get_text())

    for similar_image in soup.findAll('div', attrs={'rg_meta'}):
        tmp = json.loads(similar_image.get_text())
        img_url = tmp['ou']
        results['similar_images'].append(img_url)

    for best_guess in soup.findAll('a', attrs={'class':'fKDtNb'}):
      results['best_guess'] = best_guess.get_text()

    return json.dumps(results)

def main():
    parser = argparse.ArgumentParser(description='Meta Reverse Image Search API')
    parser.add_argument('-p', '--port', type=int, default=5000, help='port number')
    parser.add_argument('--debug', action='store_true', help='enable debug mode')
    args = parser.parse_args()

    if args.debug:
        app.debug = True

    app.run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
    main()
