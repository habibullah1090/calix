from django.contrib import admin

from .models import Adviser, Directors, Committee, Notice, Students, Teachers, Pathagar, Annual_report, Expectation
# Register your models here.


admin.site.register(Adviser)
admin.site.register(Directors)
admin.site.register(Committee)
admin.site.register(Notice)


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nick_name','phone','position' )

admin.site.register(Teachers, TeachersAdmin)


admin.site.register(Students)

admin.site.register(Pathagar)
admin.site.register(Annual_report)

admin.site.register(Expectation)
