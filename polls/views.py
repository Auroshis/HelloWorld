from django.shortcuts import render, redirect

def index(request):
    return render(request, 'base.html')

def samplepage(request):
    return render(request, 'samplepage.html')