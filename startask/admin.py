from django.contrib import admin

# Register your models here.
from startask.models import Stratask


class TimeDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', "title" , "star" ]


    class Meta:
        model = Stratask


admin.site.register(Stratask)