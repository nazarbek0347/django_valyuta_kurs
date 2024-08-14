from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
# Create your views here.
def home(request):
    r=requests.get("https://nbu.uz/en/exchange-rates/json/")
    a= json.loads(r.content)
    b=a[-1]
    return HttpResponse(f"hozirgi paytda dollir kursi {b['nbu_buy_price'][0:5]} so'mga teng")