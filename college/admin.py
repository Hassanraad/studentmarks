from django.contrib import admin
from .models import student,stage,subject,grade
from .models import Profiles
admin.site.register(student)
admin.site.register(stage)
admin.site.register(subject)
admin.site.register(grade)
# Register your models here.


class profileadmin(admin.ModelAdmin):
    pass
admin.site.register(Profiles,profileadmin)