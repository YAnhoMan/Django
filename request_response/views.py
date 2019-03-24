import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views.generic.base import View


def weather(request, area, year):
    print(area)
    print(year)
    return HttpResponse('%s,%s' % (area, year))


def query(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('hello world')


def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('hello world')


def post_json(request):
    post_str = request.body
    post_str = post_str.decode()
    post_str = json.loads(post_str)
    data = {
        'name': 'listen'
    }
    return JsonResponse(data)


class Register(View):

    def get(self, request):
        return HttpResponse('Hello Get')

    def post(self, request):
        return HttpResponse('Hello Post')
