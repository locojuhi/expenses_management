from django.contrib import admin
from apps.dt_expense.models.expense_type import ExpenseType
from apps.dt_expense.models.expense import Expense


@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'enterprise', 'expense_type')
