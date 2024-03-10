import uuid

from django.db import models

DEPARTMENT_CHOICES = [
    ('Development', 'Development'),
    ('Testing', 'Testing'),
    ('HR', 'HR'),
]


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(BaseModel):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    mobile = models.CharField(max_length=255, null=False)
    department = models.CharField(choices=DEPARTMENT_CHOICES)


class EmployeeAttendance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    is_present = models.BooleanField()
