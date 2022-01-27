from fileinput import filename
from django.shortcuts import render
from django.http import HttpResponse
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
import sys

def home(request):
    return render(request,'home.html')

def filter_selection(request):
    img=request.FILES['image']
    fs=FileSystemStorage()
    fs.delete('temp.jpeg')
    filename=fs.save('temp.jpeg',img)
    # fullurl=fs.open(filename)
    fileurl=fs.url(filename)
    return render(request,'filter_selection.html',{'raw_image':fileurl})

def result(request):
    filter=request.POST.get('filter')
    # img=request.FILES['image']
    fs=FileSystemStorage()
    # fs.delete('temp.jpeg')
    # filename=fs.save('temp.jpeg',img)
    filename='temp.jpeg'
    fullurl=fs.open(filename)
    fileurl=fs.url(filename)
    res=run([sys.executable,'templates//filter.py',str(fullurl),str(filename),filter],shell=False,stdout=PIPE)
    resurl=fs.url(str(res.stdout).split('\'')[1])
    return render(request,'result.html',{'raw_image':fileurl,'processed_image':resurl})