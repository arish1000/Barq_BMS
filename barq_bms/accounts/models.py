from django.contrib.auth.models import User
from django.db import models
from banks.models import Branch


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)