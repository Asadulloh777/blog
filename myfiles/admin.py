from django.contrib import admin
from myfiles.models import Bolim, Postlar, Sitelogo
# Register your models here.


class Adminpost(admin.ModelAdmin):
    list_display = ['id', 'bolimlar', 'nom', 'rasm', 'matn', 'aftor', 'ism', 'sana', 'vaqt']

class Adminlogo(admin.ModelAdmin):
    list_display = ['id', 'rasm_light', 'rasm_dark']

class Adminbolim(admin.ModelAdmin):
    list_display = ['id','nom','icon']

admin.site.register(Sitelogo, Adminlogo)
admin.site.register(Bolim, Adminbolim)
admin.site.register(Postlar, Adminpost)