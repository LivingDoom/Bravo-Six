from django.db import models

class Requirements(models.Model):
    pass

class ApplicationForm(models.Model):
    pass

# Create your models here.
class BenefitProgram(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(max_length=65535)
    requirements = models.ForeignKey(Requirements)
    applicationForm = models.ForeignKey(ApplicationForm)
    baseForm = models.CharField(max_length=255)

