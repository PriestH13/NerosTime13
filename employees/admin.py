from django.contrib import admin

from .models import UserProfileEmp, LeaveRequest, Shift, ShiftSwap, Message, Report, Configuration, Notification, WorkHours, Feedback

admin.site.register(UserProfileEmp)

admin.site.register(LeaveRequest)

admin.site.register(Shift)

admin.site.register(ShiftSwap)

admin.site.register(Message)

admin.site.register(Report)

admin.site.register(Configuration)

admin.site.register(Notification)

admin.site.register(WorkHours)

admin.site.register(Feedback)