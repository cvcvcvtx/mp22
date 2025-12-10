from django.contrib import admin
from .models import ActionLog
from .models import Activity

# Register your models here.

admin.site.register(Activity)
admin.site.register(ActionLog)