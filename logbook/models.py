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


