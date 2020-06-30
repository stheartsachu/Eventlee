from django.db import models

# Create your models here.
class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    email = models.CharField(unique=True, default="", max_length=200)
    password = models.CharField(max_length=50)
    def __str__(self):
        st = "%s - %s" % (self.user_id, self.first_name)
        return st

