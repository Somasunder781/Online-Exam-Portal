from django.db import models

# Create your models here.
class students(models.Model):
    sn=models.CharField(max_length=200)
    pn=models.CharField(max_length=200)
    def __str__(self):
        return self.sn
class detials(models.Model):
    prostu=models.ForeignKey(students, on_delete=models.CASCADE)
    sp=models.CharField(max_length=500)
    ps=models.CharField(max_length=500)
    def __str__(self):
        return self.sp