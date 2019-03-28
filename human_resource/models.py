from django.db import models

# Create your models here.


class HumanResource(models.Model):
    class Meta:
        permissions = (("can_access_hr","Can access HR"),)
        default_permissions = ()


