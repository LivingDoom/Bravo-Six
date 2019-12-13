from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_init = models.CharField(max_length=1, blank=True)
    last_name = models.CharField(max_length=40)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    dob = models.DateField(null=True, blank=True)
    annual_income = models.IntegerField()

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()


class Requirements(models.Model):
    pass

class ApplicationForm(models.Model):
    pass

# Create your models here.
class BenefitProgram(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(max_length=65535)
    requirements = models.ForeignKey(Requirements, on_delete=models.DO_NOTHING)
    applicationForm = models.ForeignKey(ApplicationForm, on_delete=models.DO_NOTHING)
    baseForm = models.CharField(max_length=255)

