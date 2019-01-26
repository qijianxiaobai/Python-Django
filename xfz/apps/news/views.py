from django.shortcuts import render

def index(reqiest):
    return render(reqiest, 'news/index.html')