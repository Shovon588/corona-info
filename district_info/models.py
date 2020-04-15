from django.db import models
import datetime

# Create your models here.


class DistrictInfo(models.Model):
    dist_name = models.CharField(max_length=50, unique=True)
    lat = models.DecimalField(max_digits=6, decimal_places=4)
    lon = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return self.dist_name


class CaseInfo(models.Model):
    name = models.ForeignKey(DistrictInfo, on_delete=models.CASCADE)
    cases = models.PositiveIntegerField(default=0)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return "%d new cases in %s" %(self.cases, self.name.dist_name)


class TotalInfo(models.Model):
    date = models.DateField(default=datetime.date.today())
    new_case = models.PositiveIntegerField(default=0)
    new_death = models.PositiveIntegerField(default=0)
    new_recovery = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Date: {}, Case: {}, Death: {}, Recovered: {}".format(self.date, self.new_case, self.new_death, self.new_recovery)


class DivisionInfo(models.Model):
    name = models.CharField(max_length=100)
    cases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%d cases in %s" %(self.cases, self.name)


class WebHitCounter(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now())
    counter = models.PositiveIntegerField()

    def __str__(self):
        return "Date: {}, Hit: {}" .format(self.date.date(), self.counter)
