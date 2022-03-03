from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home-main'),

    path('advisers/', views.advisers, name='advisers'),
    path('advisers/<int:id>', views.adviser, name='adviser'),

    path('directors/', views.directors, name='directors'),
    path('directors/<int:id>', views.director, name="director"),

    path('committee/', views.committee, name='committee'),

    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:id>', views.teacher, name='teacher'),

    path('lib/', views.lib, name='lib'),
    path('annualreport/', views.annualreport, name='annualreport'),

    path('expectation/', views.expectation, name='expectation'),
    path('expectation/add', views.add_expectation, name='add-expectation'),



    path('socialworks/', views.socialworks, name='socialworks'),

    path('about_us/', views.about_us, name='about_us'),
    path('started/', views.started, name='started'),
    path('kids/', views.kids, name='kids'),
    path('contact/', views.contact, name='contact'),
]
