from django.db import models

class Coder(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=40)
    IS_COOL = (
        ('Y', 'Yes'),
        ('N', 'No')
        )
    cool = models.CharField(max_length=1, choices = IS_COOL, help_text="Answer wisely")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Centre(models.Model):
    name = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=50)
        
    def __str__(self):
        fullName = self.name + " (" + self.nearest_city + ")"
        return fullName

class Climb(models.Model):
    colour = models.CharField(max_length=50)
    grade = models.CharField(max_length=6)
    centre = models.ForeignKey(Centre,related_name='climbs' , on_delete=models.CASCADE)

    def __str__(self):
        routeName = self.colour + " " + self.grade
        return routeName



