from django.contrib import admin

# Register your models here.
from .models import Message, Others, Results, Images


admin.site.register(Message)
admin.site.register(Others)
admin.site.register(Results)
admin.site.register(Images)
