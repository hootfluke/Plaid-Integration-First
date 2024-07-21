from django.db import models


#form model, id and name
class User(models.Model):
    email = models.EmailField(max_length=255, null=False, default="")
    password = models.CharField(max_length=50)
    is_logged_in = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token = models.CharField(max_length=500, null=True, blank=True)
    access_token = models.CharField(
        max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.email

