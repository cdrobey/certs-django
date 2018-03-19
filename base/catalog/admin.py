from django.contrib import admin
from catalog.models import Material, Mill, Vendor

# Register your models here.admin.site.register(Book)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'mill', 'description',
                    'date_received', 'date_sold', 'po')
    list_filter = ('date_received', 'date_sold')

    fieldsets = (
        (None, {
            'fields': ('vendor', 'mill', 'description', 'po',
                       ('date_received', 'date_sold')),
        }),
        ('UDF', {
            'fields': ('udf2', 'udf3')
        }),
        ('Heat Numbers', {
            'fields': ('heat1', 'heat2', 'heat3', 'heat4', 'heat5')
        }),
    )


admin.site.register(Material, MaterialAdmin)


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address1', 'address2', 'city', 'state', 'zipcode')


admin.site.register(Vendor, VendorAdmin)


class MillAdmin(admin.ModelAdmin):
    list_display = ('name', 'address1', 'address2', 'city', 'state', 'zipcode')


admin.site.register(Mill, MillAdmin)
