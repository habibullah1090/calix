from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ExpectationForm
from .models import Adviser, Directors, \
    Committee, Notice, Teachers, Pathagar, \
    Annual_report, Expectation


def home(request):
    return render(request, 'index.html', {
        'notice': Notice.objects.latest('id'),
    })


def advisers(request):
    return render(request, 'pages/advisers.html', {
        'advisers': Adviser.objects.all()
    })


def adviser(request, id):
    return render(request, 'pages/adviser.html', {
        'adviser': Adviser.objects.filter(pk=id).first()
    })


def directors(request):
    return render(request, 'pages/directors.html', {
        "directors": Directors.objects.all()
    })


def director(request, id):
    return render(request, 'pages/director.html', {
        "director": Directors.objects.filter(pk=id).first()
    })


def committee(request):
    return render(request, 'pages/committee.html', {
        "members": Committee.objects.all()
    })


def teachers(request):
    return render(request, 'pages/teachers.html', {
        "teachers": Teachers.objects.all()
    })


def teacher(request, id):
    return render(request, 'pages/teacher.html', {
        "teacher": Teachers.objects.filter(pk=id).first()
    })


def lib(request):
    return render(request, 'pages/lib.html', {
        "libs": Pathagar.objects.all()
    })


def annualreport(request):
    return render(request, 'pages/annualreport.html', {
        "reports": Annual_report.objects.all()
    })


def expectation(request):
    return render(request, 'pages/expectation.html', {
        "posts": Expectation.objects.all(),
        'form': ExpectationForm
    })


# need to work here
def add_expectation(request):
    if request.method == 'POST':
        print(request.POST)
    return HttpResponse('Hello world')


def socialworks(request):
    return render(request, 'pages/socialworks.html')


def about_us(request):
    return render(request, 'pages/about_us.html')


def started(request):
    return render(request, 'pages/started.html')


def kids(request):
    return render(request, 'pages/kids.html')


def contact(request):
    return render(request, 'pages/contact.html')
