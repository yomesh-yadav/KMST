from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import from_small_text_to_kb,get_desired_text

def index(request):
    return render(request,'index.html')

def get_relations(request):
    if request.method == "POST":

        query = request.POST["query"]

        text_for_kb = get_desired_text(query)
        kb = from_small_text_to_kb(text_for_kb,verbose=False)
        
        print(kb)

        data = {'entity': kb[0], 'relations': kb[1]}

    return render(request, 'graph.html', data)
