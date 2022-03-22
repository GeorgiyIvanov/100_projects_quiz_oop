import urllib.request
import ssl
import json


gcontext = ssl.SSLContext()
with urllib.request.urlopen('https://opentdb.com/api.php?amount=10&type=boolean', context = gcontext) as response:
    html = response.read()
html = html.decode('utf-8')
html = json.loads(html)

question_data = html['results']