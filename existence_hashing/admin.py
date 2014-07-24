from django.contrib import admin
from existence_hashing.models import Passport, Coop
# Register your models here.


#from existence_hashing.models import Report
#from existence_hashing.models import Coop

class PassportAdmin(admin.ModelAdmin):
    list_display =('nationality','id_passport','last_name', 'first_name')
    list_filter = ['nationality']
    search_fields = ['id_passport']

class CoopAdmin(admin.ModelAdmin):
    fields = ['country_a','country_b']
    list_display =('country_a','country_b')
    search_fields = ['country_a','country_b']

admin.site.register(Passport, PassportAdmin)
#admin.site.register(Report)
admin.site.register(Coop, CoopAdmin)
