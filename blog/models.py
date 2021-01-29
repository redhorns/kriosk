from __future__ import unicode_literals
from django.db import models

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Blog_Section(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return self.name


class Blog(models.Model) :

    fk = models.ForeignKey(Blog_Section, on_delete=models.PROTECT, null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    read_duration = models.IntegerField(null=True, blank=True)
    tag = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self) :

        if self.fk :
            return "{} ({})".format(self.title, self.fk.name)
        else :
            return "{} (None)".format(self.title)

@receiver(post_delete, sender=Blog)
def submission_delete(sender, instance, **kwargs) :
    instance.image1.delete(False)




