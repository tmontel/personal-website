from django.shortcuts import render


def cv(request):
    return render(request, 'cv/cv.html')


def about(request):
    return render(request, 'cv/about.html')