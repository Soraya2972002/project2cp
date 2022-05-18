from django.contrib import admin

# Register your models here.
from .models import Product,Feedback
class ProductAdmin(admin.ModelAdmin):
    list_display=('nometpren',)
    #exclude = ['pretaexpedier',"enramassage","entransit","enhub","enlivraison","suspendus","nonencaissés","encaissésnonpayes","paiementsprets","chezclient","retoursentraitement","retoursprets",'livreur']
    #up - in case i wanna remove fields from the admin
    search_fields = ('nometpren',)
class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product,ProductAdmin)
admin.site.register(Feedback,FeedbackAdmin)