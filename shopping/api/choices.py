from django.db import models

class Payment_choices(models.IntegerChoices):
    Paypal = 1
    Direct_check = 2
    Bank_transfer = 3

