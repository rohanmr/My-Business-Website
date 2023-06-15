from django.contrib import admin
from enroll.models import addbussi
from enroll.models import contact
# Register your models here.
class addbussiAdmin(admin.ModelAdmin):
    list_display=('name','category')
admin.site.register(addbussi,addbussiAdmin)


class contactRegister(admin.ModelAdmin):
    list_display=('name','lname')
admin.site.register(contact,contactRegister)
