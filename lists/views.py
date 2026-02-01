from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return HttpResponse('<html><head><title>To-Do Lists</title></head><body><h1>To-Do List</body></html>')