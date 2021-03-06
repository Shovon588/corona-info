from django.contrib import admin
from .models import DistrictInfo, CaseInfo, TotalInfo, DivisionInfo, WebHitCounter, DivisionName


class CaseAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'cases']
    list_filter = ['date']


class TotalAdmin(admin.ModelAdmin):
    list_display = ['date', 'new_case', 'new_death', 'new_recovery']
    list_filter = ['date']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['dist_name']


class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'cases']


# Register your models here.
admin.site.register(DistrictInfo, DistrictAdmin)
admin.site.register(CaseInfo, CaseAdmin)
admin.site.register(TotalInfo, TotalAdmin)
admin.site.register(DivisionInfo, DivisionAdmin)
admin.site.register(WebHitCounter)
admin.site.register(DivisionName)
