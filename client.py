import pycurl, json, StringIO

data = json.dumps({"image_url": "http://moviecroft.com/wp-content/uploads/2013/11/cute-earphones-anime-nyashka-kawaii.jpg", "api_key": "123"})
url = 'http://api.mrisa.mage.me.uk/search'

storage = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.PORT, 5000)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

returned_json = storage.getvalue()
print returned_json
