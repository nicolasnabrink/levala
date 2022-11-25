from django.contrib import admin

from .models import Request, Review, User, Company, Client, Admin

# Register your models here.


admin.site.register(Request)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Admin)