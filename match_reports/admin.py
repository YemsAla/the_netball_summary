from django.contrib import admin

# Register your models here.
from .models import MatchReport, Comment

admin.site.register(MatchReport)
admin.site.register(Comment)
