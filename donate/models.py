from django.db import models

# Create your models here.
from django.db import models
from accounts.models import MyUser

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    date = models.DateTimeField(auto_now=True)
    donated_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)