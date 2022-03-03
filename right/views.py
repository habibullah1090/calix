from django.shortcuts import render

from .models import Islamic_discussion, General_education, \
    Technical_education, \
    Adult_education, General_knowledge, About_student, Book_list



# middle bar


from main.models import Notice 

from extra.models import Results

def notice(request):
    return render(request, "pages/middle/notice.html", {
        "notices": Notice.objects.all()
    })


def results(request):
    return render(request, "pages/middle/results.html",{
        "results": Results.objects.all()
        })


def admission(request):
    return render(request, "pages/middle/admission.html")


def others(request):
    return render(request, "pages/middle/others.html")


# right links

def gallery(request): return render(request, 'pages/gallery.html')


def quran(request):
    return render(request, 'pages/quran.html')


def islamic(request):
    return render(request, 'pages/islamic.html', {
        "posts": Islamic_discussion.objects.all()
    })


def book_list(request):
    return render(request, 'pages/book_list.html', {
        "posts": Book_list.objects.all()
    })


def gk(request):
    return render(request, 'pages/gk.html', {
        "posts": General_knowledge.objects.all()
    })


def by_student(request):
    return render(request, 'pages/by_student.html')


def nutrition(request):
    return render(request, 'pages/nutrition.html')


def about_student(request):
    return render(request, 'pages/about_student.html', {
        "posts": About_student.objects.all()
    })

# educational activity


def general_education(request):
    return render(request, 'pages/general_education.html', {
        "posts": General_education.objects.all()
    })


def technical_education(request):
    return render(request, 'pages/technical_education.html', {
        "posts": Technical_education.objects.all()
    })


def adult_education(request):
    return render(request, 'pages/adult_education.html', {
        "posts": Adult_education.objects.all()
    })
