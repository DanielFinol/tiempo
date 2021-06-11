from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.palabra = get_random_string(length=14)

    if 'número' in request.session:
        request.session['número'] += 1
    else:
        request.session['número'] = 1

    return render(request,'random_word.html')

def reset(request):
    request.session['número'] = 0
    return redirect("/random_word")
