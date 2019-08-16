#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def count(request):
    user_text = request.GET['text']
    total_count=(len(user_text))
    return render(request,'count.html',{'count':total_count,'text':user_text})