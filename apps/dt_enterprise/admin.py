from django.contrib import admin
from apps.dt_enterprise.models.enterprise import Enterprise


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    pass
