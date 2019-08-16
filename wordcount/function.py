#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')


def count(request):
    user_text = request.GET['text']
    total_count=(len(user_text))

    word_dict={}
    for word in user_text:
        if word not in word_dict: #默认判断的是字典的键
            word_dict[word]=1
        else:
            word_dict[word]+=1



    return render(request,'count.html',
                  {'count':total_count,
                   'text':user_text,
                   'worddict':word_dict})


def about(request):
    return render(request,'about.html')
