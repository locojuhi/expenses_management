from django.db import models
from apps.dt_expense.models.expense_type import ExpenseType
from apps.dt_enterprise.models.enterprise import Enterprise


class Expense(models.Model):
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)
