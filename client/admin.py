from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Number)
admin.site.register(Address)
admin.site.register(Prompter)
admin.site.register(Contract)
admin.site.register(PassportDetails)


