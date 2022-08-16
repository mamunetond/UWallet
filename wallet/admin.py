from django.contrib import admin
from .models import Income
from .models import Spent

admin.site.register(Income)
admin.site.register(Spent)
