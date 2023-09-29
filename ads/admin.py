from django.contrib import admin
from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['publisher', 'title', 'created', 'is_public']
    list_filter = ['created']
    search_fields = ['title', 'description']
    raw_id_fields = ['publisher']
    readonly_fields = ['created']
    list_per_page = 3
