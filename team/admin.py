from django.contrib import admin
from .models import Team


class EmployeeInline(admin.TabularInline):
    model = Team.employees.through


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "employee_count", "employee_names"]
    list_filter = ["employees"]
    search_fields = ["name"]
    filter_horizontal = ("employees",)
    inlines = [EmployeeInline]

    def employee_count(self, obj):
        return obj.employees.count()

    employee_count.short_description = "Number of Employees"

    def employee_names(self, obj):
        return ", ".join([employee.get_full_name() for employee in obj.employees.all()])

    employee_names.short_description = "Employee Names"
