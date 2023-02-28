from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


# DRY - Don't Repeat Yourself

def home_page(request):
    my_title = 'My future Notes app'
    context = {"title": my_title}
    return render(request, "base.html", context=context)
