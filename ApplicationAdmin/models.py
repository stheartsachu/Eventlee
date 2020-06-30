from django.db import models

# Create your models here.
class Events(models.Model):
    eventid = models.AutoField(primary_key=True)
    eventname = models.CharField(max_length=30,null=True)
    eventcategory = models.CharField(max_length=30,null=True)
    eventdescription = models.TextField(null=True)
    eventdate = models.CharField(max_length=30,null=True)
    eventtime = models.CharField(max_length=30,null=True)
    eventlocation = models.CharField(max_length=30,null=True)
    def __str__(self):
        st = "%s - %s" % (self.eventid, self.eventname)
        return st
