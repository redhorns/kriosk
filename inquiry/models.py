from django.db import models



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



