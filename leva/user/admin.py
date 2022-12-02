from django.contrib import admin
from .models import User, Client, Company, Admin

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Admin)