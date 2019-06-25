from django.db import models

# Create your models here.


class Details(models.Model):
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    roll_no=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=128)
    email_id=models.EmailField()

    def __str__(self):
        return self.roll_no