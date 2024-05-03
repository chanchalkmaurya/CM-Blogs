from django.shortcuts import render
from django.http import HttpResponse


# Each Function is the list of Views
def index(request):
    context = {
        'title': 'Blog Homepage'
    }
    return render(request, 'index.html', context)