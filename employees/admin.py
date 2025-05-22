from django.contrib import admin

from .models import UserProfileEmp, LeaveRequest, ShiftType, Shift, WorkHours

admin.site.register(UserProfileEmp)

admin.site.register(LeaveRequest)

admin.site.register(ShiftType)

admin.site.register(Shift)

admin.site.register(WorkHours)