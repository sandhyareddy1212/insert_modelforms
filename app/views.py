from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()

    return render(request,'insert_topic.html',d)


def insert_Webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFD=WebpageModelForm(request.POST)
        if WMFD.is_valid:
            WMFD.save()

    return render(request,'insert_Webpage.html',d)


def insert_acess(request):
    AMFO=AcessRecordModelForm()
    d={'AMFO':AMFO}
    if request.method=='POST':
        AMFD=AcessRecordModelForm(request.POST)
        if AMFD.is_valid():
            AMFD.save()

    return render(request,'insert_acess.html',d)
