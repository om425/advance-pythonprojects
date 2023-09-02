import requests
import json 



url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=YOUR_KEY')

r = requests.get(url)

news = json.loads(r.text)
print (r.json())



for new in news['articles']:

    print(str(new['title']), "\n")
    # print(str(new['description',"\n\n"]))
   
