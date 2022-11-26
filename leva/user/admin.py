from django.contrib import admin

from .models import User, Client, Company, CompanyProfile, ClientProfile

admin.site.register(User)
admin.site.register(CompanyProfile)
admin.site.register(ClientProfile)
admin.site.register(Client)
admin.site.register(Company)