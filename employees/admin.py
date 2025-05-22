from django.contrib import admin

from .models import UserProfileEmp, Shift, ShiftType, WorkHours

admin.site.register(UserProfileEmp)

admin.site.register(Shift)

admin.site.register(ShiftType)

admin.site.register(WorkHours)
