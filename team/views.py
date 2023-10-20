from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Team
from .serializers import TeamAddRemoveEmployeesSerializer, TeamListSerializer, TeamSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.prefetch_related("employees")

    @action(detail=True, methods=['POST'])
    def add_employees(self, request, pk=None):
        team = self.get_object()
        serializer = TeamAddRemoveEmployeesSerializer(data=request.data)

        if serializer.is_valid():
            employee_ids = serializer.validated_data['employee_ids']
            employees = get_user_model().objects.filter(pk__in=employee_ids)

            existing_employees = team.employees.filter(pk__in=employee_ids)
            new_employees = employees.exclude(pk__in=existing_employees)

            if new_employees:
                team.employees.add(*new_employees)
                emp = ', '.join([employee.get_full_name() for employee in new_employees])
                return Response({'message': f'{emp} added to the team successfully'})
            else:
                return Response({'message': 'All specified employees are already in the team.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def remove_employees(self, request, pk=None):
        team = self.get_object()
        serializer = TeamAddRemoveEmployeesSerializer(data=request.data)

        if serializer.is_valid():
            employee_ids = serializer.validated_data['employee_ids']
            employees_to_remove = team.employees.filter(pk__in=employee_ids)

            if employees_to_remove:
                team.employees.remove(*employees_to_remove)
                emp = ', '.join([employee.get_full_name() for employee in employees_to_remove])
                return Response({'message': f'{emp} removed from the team successfully'})

            return Response({'message': 'No specified employees were found in the team.'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ['add_employees', 'remove_employees']:
            return TeamAddRemoveEmployeesSerializer
        elif self.action == "list":
            return TeamListSerializer
        return TeamSerializer
