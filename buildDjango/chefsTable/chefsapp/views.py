from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def menuitems(request, dish):
#     items = {
#         'pasta': 'Pasta is a type of noodle',
#         'falafel': 'Falafel are deep fried patties',
#         'chessecake': 'Chessecake is a type of dessert'
#     }

#     description = items[dish]

#     return HttpResponse(f"<h2> {dish} </h2>" + description)


def home(request):
    return HttpResponse('Hello, World!')


# def homepage(request):
#     return HttpResponse('Welcome to Little Lemon!')


# def display_date(request):
#     date_joined = datetime.today().year
#     return HttpResponse(date_joined)


# def menu(request):
#     text = """<h1 style="color: #F4CE14;"> This is Little Lemon again!</h1>"""
#     return HttpResponse(text)
