from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index(request):
    # return HttpResponse(f"Hi")
    return render(request, "index.html")

def compute_square(request, number):
    square = number * number
    context = {"square": square, "number": number}
    return render(request, "compute_square.html", context=context)

def compute_squares(request, number):
    numbers = list(range(number))
    squares = [n**2 for n in numbers]
    context = {
        "number_and_square": [
            {"number": number, "square": square}
            for number, square in zip(numbers, squares)
        ]
    }
    return render(request, "compute_squares.html", context=context)

def random_wiki(request):
    url = 'https://en.wikipedia.org/wiki/Special:RandomInCategory/Featured_articles'
    response = requests.get(url)
    
    content = response.content
    
    soup = BeautifulSoup(content, 'html.parser')
    
    page_title = soup.find('h1', {'class': 'firstHeading'}).text

    language_list = soup.find('div', {'id': 'p-lang-btn'})
    
    if language_list:
        language_links = language_list.find_all('a')
        languages = [lang.text for lang in language_links]
        languages.pop(-1)
    else:
        languages = []

    context = {
        "title": page_title,
        "languages": languages,
    }
    return render(request, 'random_wiki.html', context=context)
