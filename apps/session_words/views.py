from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    return render(request, 'session_words/index.html')

def process(request):
    if "list" not in request.session:
        request.session['list'] = []
    postInfo = {
        "word":request.POST['word'],
        "color":request.POST['color'],
        "day": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
    }
    if "big" in request.POST:
        postInfo['big'] = request.POST['big']
    print postInfo['day']
    print postInfo['time']
    request.session['list'].append(postInfo)
    request.session.modified = True
    return redirect('/session_words/')

def clear(request):
    request.session.clear()
    return redirect('/session_words/')