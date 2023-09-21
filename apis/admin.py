from django.contrib import admin
from .models import Province, District, LocalGovernment


admin.site.register(Province)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']
    
admin.site.register(District,DistrictAdmin)

class LocalGovernmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']
    
admin.site.register(LocalGovernment,LocalGovernmentAdmin)
