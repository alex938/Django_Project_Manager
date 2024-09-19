from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/index.html')