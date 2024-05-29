from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    dp = models.ImageField(upload_to='uploads/')


class Metric(models.Model):
    empno = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None)
    check_in = models.CharField(max_length=20)
    check_out = models.CharField(max_length=20)
    error_rate = models.FloatField()
    submission_status = models.BooleanField(default=False)