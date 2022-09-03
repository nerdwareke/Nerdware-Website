from django.db import models

# Create your models here.
class Position(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        phone = models.CharField(max_length=100)
        company_name = models.CharField(max_length=100)
        where_did_you_find_us = models.CharField(max_length=100)
        applyfor = models.CharField(max_length=100)
        website_url = models.CharField(max_length=100)
        message = models.CharField(max_length=100)
        file = models.FileField(upload_to='Position_Files/%Y/%m/%D/', blank=True, null=True)

class Projects(models.Model):
        name = models.CharField(max_length=100)
        email = models.CharField(max_length=100)
        phone = models.CharField(max_length=100)
        company_name = models.CharField(max_length=100)
        where_did_you_find_us = models.CharField(max_length=100)
        budget = models.CharField(max_length=100)
        website_url = models.CharField(max_length=100)
        message = models.CharField(max_length=100)
        file = models.FileField(upload_to='Project_Files/%Y/%m/%D/', blank=True, null=True)

class Documents(models.Model):
        name = name = models.CharField(max_length=100)
        file = models.FileField(upload_to='Nerdware_Files/', blank=True, null=True)