from django.db import models

class calc(models.Model):
    id = models.AutoField
    Time = models.CharField(max_length=30)
    field1 = models.FloatField(max_length=10)
    field2 = models.FloatField(max_length=10)
    field3 = models.FloatField(max_length=10)
    field4 = models.FloatField(max_length=10)
    field5 = models.FloatField(max_length=10)
    field6 = models.FloatField(max_length=10)
    field7 = models.FloatField(max_length=10)
    field8 = models.FloatField(max_length=10)

    def __str__(self):
        return str(self.id)
# Create your models here.
