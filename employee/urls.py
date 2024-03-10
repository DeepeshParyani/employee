from django.urls import path
from rest_framework.routers import DefaultRouter
from employee.views import EmployeeListView, EmployeeAddView, EmployeeDeleteView, EmployeeUpdateView, \
    EmployeeAllAttendanceView, EmployeeTodayAttendanceListView, EmployeeTodayAttendanceUpdateView

router = DefaultRouter()
app_name = "employee"

urlpatterns = [
    path('add/', EmployeeAddView.as_view(), name='employee-add'),
    path('list/', EmployeeListView.as_view(), name='employee-list'),
    path('delete/<str:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('update/<str:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('all-attendance/', EmployeeAllAttendanceView.as_view(), name='all-attendance'),
    path('today-attendance-list/', EmployeeTodayAttendanceListView.as_view(), name='today-attendance-list'),
    path('today-attendance-update/', EmployeeTodayAttendanceUpdateView.as_view(), name='today-attendance-update'),
]
urlpatterns += router.urls
