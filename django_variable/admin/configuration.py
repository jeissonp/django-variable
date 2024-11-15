from django.contrib import admin
from apps.variable_config.models.configuration import Configuration

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['key', 'value']
    search_fields = ('key', 'value')