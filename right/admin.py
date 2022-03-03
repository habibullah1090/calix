from django.contrib import admin

from .models import Islamic_discussion, General_education, Technical_education,Adult_education, General_knowledge, About_student

# Register your models here.
admin.site.register(Islamic_discussion)
admin.site.register(General_education)
admin.site.register(Technical_education)
admin.site.register(Adult_education)
admin.site.register(General_knowledge)
admin.site.register(About_student)