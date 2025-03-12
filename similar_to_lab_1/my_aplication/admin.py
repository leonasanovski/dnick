from django.contrib import admin

from my_aplication.models import Vehicle, Repairment, WorkplaceForManufacturers, Manufacturer, Workplace

# Register your models here.
class WorkplaceForManufacturersInline(admin.TabularInline):
    model = WorkplaceForManufacturers
    extra = 1
class WorkplaceAdmin(admin.ModelAdmin):
    list_displays = ["name","year_founded","repairs_oldTimers"]
    inlines = [WorkplaceForManufacturersInline]
class RepairmentAdmin(admin.ModelAdmin):
    exclude = ("user_reported",)
    def save_model(self, request, obj, form, change):
        obj.user_reported = request.user
        return super(RepairmentAdmin, self).save_model(request, obj, form, change)
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
class ManufacturerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Repairment,RepairmentAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Workplace,WorkplaceAdmin)
admin.site.register(Vehicle)