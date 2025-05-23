from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfileEmp(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    role = models.CharField(max_length=50, choices=[('ADMIN', 'Administrator'), ('EMPLOYEE', 'Employee')])
    employee_id = models.CharField(max_length=20, unique=True)
    hire_date = models.DateField()
    available_leave_days = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.employee_id})"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class LeaveRequest(models.Model):

    LEAVE_TYPES = [
        ('SICK', 'Sick Leave'),
        ('VACATION', 'Vacation Leave'),
        ('PERSONAL', 'Personal Leave'),
        ('UNPAID', 'Unpaid Leave'),
    ]
    REQUEST_STATUS = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(UserProfileEmp, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='PENDING')
    request_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)
    approver = models.ForeignKey(UserProfileEmp, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    def duration(self):
        return (self.end_date - self.start_date).days + 1
    def __str__(self):
        return f"{self.leave_type} leave by {self.user} from {self.start_date} to {self.end_date}"

    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"


# This model is used to define the types of shifts available in the system.(E.g., Morning, Evening, Night)
class ShiftType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shift Type"
        verbose_name_plural = "Shift Types"


class Shift(models.Model):
    user = models.ForeignKey(UserProfileEmp, on_delete=models.CASCADE, related_name='shifts')
    date = models.DateField()
    shift_type = models.ForeignKey(ShiftType, on_delete=models.CASCADE, related_name='shifts')
    description = models.CharField(max_length=200, blank=True, null=True)

    @property
    def start_time(self):
        return self.shift_type.start_time

    @property
    def end_time(self):
        return self.shift_type.end_time

    def __str__(self):
        return f"{self.shift_type.name} shift for {self.user} on {self.date} ({self.start_time} - {self.end_time})"

    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"


class WorkHours(models.Model):
    user = models.ForeignKey(UserProfileEmp, on_delete=models.CASCADE, related_name='work_hours')
    date = models.DateField()
    hours_worked = models.FloatField(default=0.0)
    overtime_hours = models.FloatField(default=0.0)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Work hours for {self.user} on {self.date}: {self.hours_worked}h (Overtime: {self.overtime_hours}h)"

    class Meta:
        verbose_name = "Work Hours"
        verbose_name_plural = "Work Hours"
