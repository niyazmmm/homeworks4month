from django.shortcuts import HttpResponse
import datetime

# Create your views here.


def first_view(request):
    if request.method == 'GET':
        return HttpResponse("This is the main page!")


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def now_date_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now())


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")

