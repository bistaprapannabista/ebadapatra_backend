from django.contrib import admin
from .models import Province, District, LocalGovernment, Document, Service
import json

admin.site.register(Province)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']
    
admin.site.register(District,DistrictAdmin)

class LocalGovernmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']
    
admin.site.register(LocalGovernment,LocalGovernmentAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
admin.site.register(Document,DocumentAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name","documents_list","price","time","responsible_person"]
    search_fields = ["name"]

    def documents_list(self,obj):
        return ", ".join([document.name for document in obj.documents.all()])

admin.site.register(Service,ServiceAdmin)