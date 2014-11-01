from django.db import models
from django.contrib.auth.models import User

class ABExperiment(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    action_url=models.CharField(max_length=200)
    initial_date = models.DateTimeField()
    def __str__(self):
        return self.name
    

class ExperimentAd(models.Model):
    experiment = models.ForeignKey(ABExperiment, default=1)  
    name = models.CharField(max_length=200)
    src_url = models.CharField(max_length=200)
    visits = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

