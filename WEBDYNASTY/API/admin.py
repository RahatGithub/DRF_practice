from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Station)
admin.site.register(Ticket)
admin.site.register(Stop)
admin.site.register(Train)