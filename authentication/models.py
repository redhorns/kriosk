from django.db import models
from django.contrib.auth.models import User




class Auth_Code(models.Model) :

    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    auth_code = models.IntegerField(null=True, blank=True)
    auth_is_used = models.BooleanField(default=False, null=True, blank=True)
    auth_is_flagged = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) :
        if self.auth_user :
            return self.auth_user.username
        else :
            return self.pk
