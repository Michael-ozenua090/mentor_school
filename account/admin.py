from django.contrib import admin

from account.models import CustomUser, Score

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Score)
