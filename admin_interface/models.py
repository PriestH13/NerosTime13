# from django.db import models
# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class UserProfile(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
#     role = models.CharField(max_length=50, choices=[('ADMIN', 'Administrator'), ('EMPLOYEE', 'Employee')])
#     employee_id = models.CharField(max_length=20, unique=True)
#     hire_date = models.DateField()
#     available_leave_days = models.IntegerField(default=20)

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name} ({self.employee_id})"

#     class Meta:
#         verbose_name = "User Profile"
#         verbose_name_plural = "User Profiles"


# class LeaveRequest(models.Model):
#     LEAVE_TYPES = [
#         ('SICK', 'Sick Leave'),
#         ('VACATION', 'Vacation Leave'),
#         ('PERSONAL', 'Personal Leave'),
#         ('UNPAID', 'Unpaid Leave'),
#     ]
#     REQUEST_STATUS = [
#         ('PENDING', 'Pending'),
#         ('APPROVED', 'Approved'),
#         ('REJECTED', 'Rejected'),
#     ]

#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leave_requests')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='PENDING')
#     request_date = models.DateTimeField(default=timezone.now)
#     notes = models.TextField(blank=True, null=True)
#     approver = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')

#     def __str__(self):
#         return f"Leave request by {self.user} from {self.start_date} to {self.end_date}"

#     class Meta:
#         verbose_name = "Leave Request"
#         verbose_name_plural = "Leave Requests"


# class Shift(models.Model):

#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='shifts')
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     description = models.CharField(max_length=200, blank=True, null=True)
#     priority = models.IntegerField(default=1)  # 1 = Normal, 2 = High, 3 = Critical

#     def __str__(self):
#         return f"Shift for {self.user} on {self.date} ({self.start_time} - {self.end_time})"

#     class Meta:
#         verbose_name = "Shift"
#         verbose_name_plural = "Shifts"


# class ShiftSwap(models.Model):

#     SWAP_STATUS = [
#         ('PENDING', 'Pending'),
#         ('APPROVED', 'Approved'),
#         ('REJECTED', 'Rejected'),
#     ]

#     requester_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='swap_requests')
#     proposed_shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='swap_proposals')
#     requester = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='swap_requests_made')
#     recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='swap_requests_received')
#     status = models.CharField(max_length=20, choices=SWAP_STATUS, default='PENDING')
#     request_date = models.DateTimeField(default=timezone.now)
#     notes = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Shift swap between {self.requester} and {self.recipient}"

#     class Meta:
#         verbose_name = "Shift Swap"
#         verbose_name_plural = "Shift Swaps"


# class Message(models.Model):

#     sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_messages')
#     subject = models.CharField(max_length=200)
#     content = models.TextField()
#     sent_date = models.DateTimeField(default=timezone.now)
#     read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Message from {self.sender} to {self.recipient}: {self.subject}"

#     class Meta:
#         verbose_name = "Message"
#         verbose_name_plural = "Messages"


# class Report(models.Model):

#     REPORT_TYPE = [
#         ('ATTENDANCE', 'Attendance'),
#         ('WORK_HOURS', 'Work Hours'),
#         ('SHIFT_BALANCE', 'Shift Balancing'),
#     ]

#     report_type = models.CharField(max_length=50, choices=REPORT_TYPE)
#     generated_date = models.DateTimeField(default=timezone.now)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reports', null=True, blank=True)
#     data = models.JSONField()  # To store structured report data
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Report {self.report_type} - {self.generated_date}"

#     class Meta:
#         verbose_name = "Report"
#         verbose_name_plural = "Reports"


# class Configuration(models.Model):

#     key = models.CharField(max_length=100, unique=True)  # e.g., 'holidays_2025', 'admin_permissions'
#     value = models.TextField()  # JSON or text for flexible configurations
#     description = models.CharField(max_length=200, blank=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Configuration: {self.key}"

#     class Meta:
#         verbose_name = "Configuration"
#         verbose_name_plural = "Configurations"