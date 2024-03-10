from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from employee.forms import EmployeeForm, AttendanceUpdateForm
from employee.models import Employee, EmployeeAttendance


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'


class EmployeeAddView(CreateView):
    model = Employee
    template_name = 'employee_create.html'
    fields = ["name", "email", "mobile", "department"]
    success_url = '/employee/list/'


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee:employee-list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_update.html'
    success_url = reverse_lazy('employee:employee-list')


class EmployeeAllAttendanceView(ListView):
    model = EmployeeAttendance
    template_name = 'employees_all_attendance.html'
    context_object_name = 'employees_attendance'


class EmployeeTodayAttendanceListView(ListView):
    model = EmployeeAttendance
    template_name = 'employees_current_attendance.html'
    context_object_name = 'employees_attendance'


class EmployeeTodayAttendanceUpdateView(View):
    template_name = 'update_employees_current_attendance.html'

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        AttendanceUpdateFormSet = formset_factory(AttendanceUpdateForm, extra=0)

        # Create a formset with initial data for each employee
        formset = AttendanceUpdateFormSet(
            initial=[{'employee_id': employee.id, "employee_name": employee.name} for employee in employees])
        return render(request, self.template_name, {'employees': employees, 'formset': formset})

    def post(self, request, *args, **kwargs):
        AttendanceUpdateFormSet = formset_factory(AttendanceUpdateForm, extra=0)
        formset = AttendanceUpdateFormSet(request.POST)

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.save()
            return redirect('employee:employee-list')
        else:
            return redirect('employee:today-attendance-list')
