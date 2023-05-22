from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    reqapi = requests.get('http://api.mediastack.com/v1/news?access_key=4c9ef10d7b1b2ac426bd8d3ce78a518b&countries=au,-us')
    resapi = reqapi.json()
    data = resapi["data"]
    title = []
    description = []
    image = []
    author = []
    url = []
    for news in data:
        title.append(news['title'])
        image.append(news['image'])
        description.append(news['description'])
        author.append(news['author'])
        url.append(news['url'])
    newszip = zip(title, description, image, author, url)
    return render(request, 'enewscode/index.html', {'newszip': newszip})