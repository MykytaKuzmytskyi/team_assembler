from django.contrib.auth import get_user_model
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
            team.employees.add(*employees)
            return Response({'message': 'Employees added to the team successfully'})

        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['POST'])
    def remove_employees(self, request, pk=None):
        team = self.get_object()
        serializer = TeamAddRemoveEmployeesSerializer(data=request.data)

        if serializer.is_valid():
            employee_ids = serializer.validated_data['employee_ids']
            employees = get_user_model().objects.filter(pk__in=employee_ids)
            team.employees.remove(*employees)
            return Response({'message': 'Employees removed from the team successfully'})

        return Response(serializer.errors, status=400)

    def get_serializer_class(self):
        if self.action in ['add_employees', 'remove_employees']:
            return TeamAddRemoveEmployeesSerializer
        elif self.action == "list":
            return TeamListSerializer
        return TeamSerializer
