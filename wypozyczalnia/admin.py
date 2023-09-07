from django.contrib import admin

from .models import *

admin.site.register(Rental)
admin.site.register(Books)
admin.site.register(Movies)
admin.site.register(CD)
admin.site.register(Songs)