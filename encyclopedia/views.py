from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
import random
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,entry):
    markdown = Markdown()
    entryPage = util.get_entry(entry)
    if entryPage == None:
        return render(request, "encyclopedia/none.html", 
        {"title": entry, "message": "No Such entry"})
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown.convert(entryPage),
            "title": entry
        })

class NewSearchForm(forms.Form):
    search = forms.CharField()

def convert(title):
    entry = util.get_entry(title)
    if entry is not None:
        markdown = Markdown()
        return markdown.convert(entry)
    else: 
        return None

def search(request): 
    if request.method == "POST":
        search = request.POST['q']
        entry = convert(search)
        if entry is not None:
            return render(request, "encyclopedia/entry.html", {
                "entry": entry,
                "title": search
            })
        else:
            recommendation = []
            all_entries = util.list_entries()
            for single_entry in all_entries:
                if search.lower() in single_entry.lower():
                    recommendation.append(single_entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })

def create(request): 
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        
        if title in [x.lower() for x in util.list_entries()]:
            return render(request, "encyclopedia/none.html", {
                "title": title, 
                "message": "Already exisiting title"
            })
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "entry": content
            })
    return render(request, "encyclopedia/create.html")
        