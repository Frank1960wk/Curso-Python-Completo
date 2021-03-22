from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime
from django.views import View
from django.views.generic import ListView
from .models import Entry

def dummy_view(request):
    return render(request,"posts/post_list.html", {})

def status_code_view(request):
    return render(request,"posts/post_list.html", {})

def entry_list(request):
    return render(request,"posts/post_list.html", {})

def redirect_back_home(request):
    return redirect('http://datadosis.com')

class MyClassView(View):
    def get(self, request):
        print("correr codigo")
        return HttpResponse("Response from a CBV")

class MyListView(ListView):
    model = Entry