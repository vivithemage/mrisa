import pycurl, json, StringIO

data = json.dumps({"name": "test_repo", "description": "Some test repo"})
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
