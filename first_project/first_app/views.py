from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    dict1 = { 'insert_me':"Hello this is insert me babe" }
    return render(request,'index.html',context=dict1)