from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey_app/index.html')

def process(request):
    if "counter" not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    request.session['post'] = request.POST
    return redirect("/survey_app/result/")

def result(request):
    return render(request, 'survey_app/result.html')