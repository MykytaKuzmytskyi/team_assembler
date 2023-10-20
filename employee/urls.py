from django.urls import path

from .views import CreateEmployeeView, EmployeeListView, EmployeeDetailView

app_name = "employee"

urlpatterns = [
    path("create_employee/", CreateEmployeeView.as_view(), name="create_employee"),
    path("employees/", EmployeeListView.as_view(), name="employee_list"),
    path("employee/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),
]
