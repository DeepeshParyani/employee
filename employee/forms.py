from django import forms

from employee.models import Employee, EmployeeAttendance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        form_class = "employee_list.html"
        fields = ['name', 'email', 'mobile', 'department']


class EmployeeAttendanceForm(forms.ModelForm):
    class Meta:
        model = EmployeeAttendance
        form_class = "update_employees_current_attendance.html"
        fields = ['is_present']


class AttendanceUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeAttendance
        fields = ['is_present']

    employee_id = forms.IntegerField(widget=forms.HiddenInput())
    employee_name = forms.CharField(widget=forms.HiddenInput())


# class AttendanceUpdateForm(forms.Form):
#     is_present = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput())
#
#     def __init__(self, *args, **kwargs):
#         employee_instance = kwargs.pop('employee_instance', None)
#         super(AttendanceUpdateForm, self).__init__(*args, **kwargs)
#
#         if employee_instance:
#             # Retrieve the existing attendance for the employee
#             existing_attendance = EmployeeAttendance.objects.filter(employee=employee_instance).first()
#
#             # Set the initial value based on existing data
#             if existing_attendance:
#                 self.fields['is_present'].initial = existing_attendance.is_present