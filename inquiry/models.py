from __future__ import unicode_literals
from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver



class Contact(models.Model) :

    name = models.CharField(max_length=150, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    service = models.CharField(max_length=150, null=True, blank=True)
    budget = models.CharField(max_length=150, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self) :
        return self.name + " | " + self.email + " ( pk = " + str(self.pk) + " )"



class Newsletter(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) :
        return self.email



class Career(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    position_name = models.CharField(max_length=200, null=True, blank=True)
    position_number = models.IntegerField(null=True, blank=True)
    position_requirement = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) :
        return self.position_name + " ( " + str(self.pk) + " )"

        

class Applicants(models.Model) :

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) :
        return self.name + " For " + self.position 

@receiver(post_delete, sender=Applicants)
def submission_delete(sender, instance, **kwargs) :
    instance.resume.delete(False)



class Free_Trial(models.Model) :

    email = models.CharField(max_length=150, null=True, blank=True)
    date = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) :
        return self.email


