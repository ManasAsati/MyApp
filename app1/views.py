from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from datetime import datetime

def hello(request):
    return HttpResponse("Manas Asati welcomes you. Have a great day!")

def login(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "Login.html", context)

def clock(request):
    now = datetime.now()
    format = '%H:%M:%S %p'
    current_time = now.strftime(format)
    current_date = now.strftime('%d-%m-%Y')
    context = {'time':current_time, 'date':current_date}
    return render(request, 'Clock.html', context)