from rest_framework import serializers

from employee.serializers import EmployeeSerializer
from team.models import Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name', 'employees']


class TeamListSerializer(TeamSerializer):
    employees = serializers.StringRelatedField(many=True)


class TeamAddRemoveEmployeesSerializer(serializers.Serializer):
    employee_ids = serializers.ListField(
        required=True,
    )
