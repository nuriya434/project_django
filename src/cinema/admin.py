from django.contrib import admin

from django.contrib import admin
from .models import Session, Movie, Hall, Director

admin.site.register(Movie)
admin.site.register(Session)
admin.site.register(Hall)
admin.site.register(Director)