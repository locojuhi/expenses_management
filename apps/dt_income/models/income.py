from django.db import models
from apps.dt_income.models.income_type import IncomeType


class Income(models.Model):
    income_type = models.ForeignKey(IncomeType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return str(self.amount)
