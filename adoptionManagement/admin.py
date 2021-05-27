from django.contrib import admin
from adoptionManagement.models import Dog, Requests, AdoptionQueue
# Register your models here.
admin.site.register(Dog)
admin.site.register(Requests)
admin.site.register(AdoptionQueue)