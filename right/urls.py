from django.urls import path
from .views import *


app_name = "right"
urlpatterns = [
    path('notice/', notice, name="notice"),
    path('results/', results, name="results"),
    path('admission/', admission, name="admission"),
    path('others/', others, name="others"),

    path('gallery/', gallery, name="gallery"),

    # student-corner
    path('quran/', quran, name="quran"),
    path('islamic/', islamic, name="islamic"),
    path('book_list/', book_list, name="book_list"),
    path('gk/', gk, name="gk"),
    path('by_student/', by_student, name="by_student"),
    path('nutrition/', nutrition, name="nutrition"),
    path('about_student/', about_student, name="about_student"),
    path('general_education/', general_education, name="general_education"),
    path('technical_education/', technical_education, name="technical_education"),
    path('adult_education/', adult_education, name="adult_education"),

]
