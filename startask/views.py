from django.shortcuts import render
from startask.models import Tasks

# Create your views here.


def mainpage(request):
    varaible = Tasks.objects.all()

    # print(varaible)
    context ={ "tasks" : varaible}
    return render(request,"main.html",context=context)


def tasks(request):
    varaible = Tasks.objects.all()
    context = {"tasks": varaible}
    return render(request, "tasks.html", context=context)