from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.

class MyBetModel(models.Model):
    race_time = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)], null=True)
    race_place = models.CharField(max_length=10)
    race_nums = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    race_bet_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(18)])
    create_at = models.DateTimeField(default=timezone.now)
    race_on_time = models.DateTimeField()
