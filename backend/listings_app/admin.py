from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps
from .models import User, Listing


class UserAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['username', 'full_name', 'email', 'verified']


admin.site.register(User, UserAdmin)

models = apps.get_models()
already_registered = admin.site._registry.keys()

for model in models:
    try:
        if model not in already_registered:
            admin.site.register(model)
    except AlreadyRegistered:
        pass
