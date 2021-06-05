from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def random_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] = request.session['count']+ 1
    request.session['unique_id'] = get_random_string(length=32, allowed_chars='ABC')
    return render(request, 'random.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')

