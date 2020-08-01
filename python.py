import urllib.request
import json

url = 'https://api.datamuse.com/words?rel_trg=cow'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

