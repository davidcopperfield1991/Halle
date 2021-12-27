from django.shortcuts import render
from startask.models import Stratask

# Create your views here.


def mainpage(request):
    varaible = Stratask.objects.all()

    # print(varaible)
    context ={ "tasks" : varaible}
    return render(request,"main.html",context=context)


def tasks(request):
    varaible = Stratask.objects.all()
    context = {"tasks": varaible}
    return render(request, "tasks.html", context=context)