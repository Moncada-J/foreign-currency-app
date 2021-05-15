from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Currency: 
    def __init__(self, country_name, currency_name, amount, obverse, description):
        self.country_name = country_name
        self.currency_name = currency_name
        self.amount = amount
        self.obverse = obverse
        self.description = description
currencies = [
        Currency('Nicaragua', 'Córdoba', 100, 'Rubén Darío', 'This was the first foreign currency I ever recieved. Collected in 2017.'),
        Currency('Canada', 'Candian Dollar', 50, 'William yon Mackenzie King',
                 "I recieved this while visiting Vancouver for the Jonas Brother's Concert! Collected in 2020."),
        Currency('United States', 'United States Dollar', 1, 'Sacagawea',
                 'I found this dollar coin on a hike and have kept it ever since. Collected in 2021.')
    ]
def home(request):
    return HttpResponse('<nav><img src="https://imgur.com/PPaJpDC.png"><h3>Collect Foreign Currencies</h3></nav>')

def about(request):
    return render(request, 'about.html')

def currencies_index(request):
    return render(request, 'currencies/index.html', {'currencies': currencies})
