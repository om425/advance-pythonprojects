import requests
import json 



url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=63269cd315bd49838e9c987260d3f67b')

r = requests.get(url)

news = json.loads(r.text)
print (r.json())



for new in news['articles']:

    print(str(new['title']), "\n")
    # print(str(new['description',"\n\n"]))
   