from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.


def index(request):
    print('view 视图被调用')
    # return HttpResponse("Hello the world!")
    response = HttpResponse()
    response.content = "Hello the world!"
    response.status_code = HttpResponseNotFound.status_code
    return response
    # return HttpResponse(content='hello world', content_type='text/html', status=200)


def say(request):
    url = reverse("users:index")
    print(url)
    return HttpResponse('say')
