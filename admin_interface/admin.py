from django.contrib import admin
from django.contrib import admin
from .models import UserProfile, LeaveRequest, Shift,ShiftSwap, Message, Report, Configuration


admin.site.register(UserProfile)

admin.site.register(LeaveRequest)

admin.site.register(Shift)

admin.site.register(ShiftSwap)

admin.site.register(Message)

admin.site.register(Report)

admin.site.register(Configuration)
