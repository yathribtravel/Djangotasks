from django.contrib import admin
from .models import stydent
# Register your models here.
# admin.site.register(stydent)
@admin.register(stydent)
class stydent_admin(admin.ModelAdmin):
    readonly_fields =["slug"]
    # prepopulated_fields = {"slug": ["name"]}