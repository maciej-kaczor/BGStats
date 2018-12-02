from django.contrib import admin

from .models import Boardgame, Designer

admin.site.register(Boardgame)
admin.site.register(Designer)