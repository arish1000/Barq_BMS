from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    is_islamic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
