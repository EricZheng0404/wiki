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
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown.convert(entryPage),
        "title": entry
    })