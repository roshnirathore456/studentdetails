from django.db import models
# Create your models here.


class Details(models.Model):
    firstname = models.CharField(max_length=20, default='', null=False)
    lastname = models.CharField(max_length=30, default='', null=False)
    useremail = models.EmailField(max_length=30, default='', null=False)
    graduation = models.CharField(max_length=30, default='', null=False)
    phone = models.CharField(max_length=14, default='', null=False)
    activityname = models.CharField(max_length=14, default='', null=False)
    activityassigned = models.CharField(max_length=30, default=' ', null=False)

    def __str__(self):
        return self.firstname

