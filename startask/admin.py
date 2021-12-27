from django.contrib import admin

# Register your models here.
from startask.models import Tasks , Routines , Stars


class TimeDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', "title" , "star" ]


    class Meta:
        model = Tasks


admin.site.register(Tasks )
admin.site.register(Stars)
admin.site.register( Routines)