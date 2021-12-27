from django.db import models
from datetime import date
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

class Stratask(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, default=date.today)
    star_expected = models.IntegerField(blank=True,null=True)
    description = models.CharField(max_length=200 ,  blank=True,null=True)
    routine = models.CharField(max_length=200 , blank=True,null=True)
    status = models.CharField(max_length=9, choices= STATUS_CHOICES)
    importance = models.IntegerField(blank=True,null=True , choices=IMPORTANCE_CHOICES)
    progress = models.CharField(blank=True,null=True , choices=PROGRESS_CHOICES,max_length=200)
    star = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Stratask"
        verbose_name = "Stratask"