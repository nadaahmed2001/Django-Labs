from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(verbose_name="Class Name", max_length=50, unique=True)
    subject = models.CharField(max_length=50)
    year = models.IntegerField(verbose_name="Year")

class AreaCalculator(models.Model):
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()

    def calculate_area(self):
        return self.width * self.height * self.length
