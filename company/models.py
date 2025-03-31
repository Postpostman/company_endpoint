from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, unique=True)
    company_address = models.TextField(blank=True, null=True)
    company_email = models.EmailField(unique=True)
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='company_user1', blank=True, null=True)
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='company_user2', blank=True, null=True)
    user3 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='company_user3', blank=True, null=True)

    def __str__(self):
        return self.company_name
