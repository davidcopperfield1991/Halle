

from django.db import models
from datetime import date, datetime

# Create your models here.

STATUS_CHOICES = (
    ("to do ", "TO DO"),
    ("doing", "DOING"),
    ("done", "DONE"),
)
IMPORTANCE_CHOICES = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
)
PROGRESS_CHOICES = (
    ("10%", "10%"),
    ("20%", "20%"),
    ("30%", "30%"),
    ("40%", "40%"),
    ("50%", "50%"),
    ("60%", "60%"),
    ("70%", "70%"),
    ("80%", "80%"),
    ("90%", "90%"),
    ("100%", "100%"),
)

class Routines(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Routines"
        verbose_name = "Routine"

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, default=date.today)
    star_expected = models.IntegerField(blank=True,null=True)
    description = models.CharField(max_length=200 ,  blank=True,null=True)
    routine = models.ForeignKey(Routines , blank=True, on_delete=models.CASCADE , null=True)
    status = models.CharField(max_length=9, choices= STATUS_CHOICES)
    importance = models.IntegerField(blank=True,null=True , choices=IMPORTANCE_CHOICES)
    progress = models.CharField(blank=True,null=True , choices=PROGRESS_CHOICES,max_length=200)

    def __str__(self):
        return self.title

    def __int__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Tasks"
        verbose_name = "Task"


class Stars(models.Model):
    date = models.DateField(blank=True, default=date.today)
    time = models.DateTimeField(default=datetime.now, blank=True)
    task_id = models.ForeignKey(Tasks, blank=True, on_delete=models.CASCADE , null=True)
    routine_name = models.ForeignKey(Routines , blank=True, on_delete=models.CASCADE , null=True)
    star = models.IntegerField(blank=True,null=True,default=1)


    def __str__(self):
        return self.task_id

    class Meta:
        verbose_name_plural = "Stars"
        verbose_name = "Star"