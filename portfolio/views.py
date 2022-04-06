from django.shortcuts import render
from .models import Project
from django.http import HttpResponseRedirect
from django.utils import translation
from django.views.generic.base import View
from django.conf import settings
from django.shortcuts import redirect


def home(request):
    return render(request, 'portfolio/home.html')


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
