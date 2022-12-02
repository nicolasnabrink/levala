from django.contrib import admin
from .models import User, Client, Company, Admin, Pedido, Comment

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Admin)
admin.site.register(Pedido)
admin.site.register(Comment)