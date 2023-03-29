from django.shortcuts import render
from django.http import HttpResponse
def pg(request):
    return HttpResponse('<h1 align="center"> i am staying in sri lakshmivenkateshwara 5* pg </h1>')

def budili(request):
    return HttpResponse('<b><marquee><i> BUDILI IS MY NATIVE</i></marquee></b>')
def sql(request):
    return HttpResponse('sql stands for structure query language')