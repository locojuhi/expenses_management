from django.contrib import admin
from apps.dt_income.models.income_type import IncomeType
from apps.dt_income.models.income import Income


@admin.register(IncomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'income_type')
