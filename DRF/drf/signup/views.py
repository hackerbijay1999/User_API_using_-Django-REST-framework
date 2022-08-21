from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from signup.serializers import DepartmentSerializer, OrganisationSerializer, ModulesSerializer, UserSerializer
from signup.models import Department, Organisation,  Modules, User

class DepartmentViewSet(viewsets.ModelViewSet):
   queryset = Department.objects.all()
   serializer_class = DepartmentSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
   queryset = Organisation.objects.all()
   serializer_class = OrganisationSerializer


class  ModulesViewSet(viewsets.ModelViewSet):
   queryset =  Modules.objects.all()
   serializer_class =  ModulesSerializer


class  UserViewSet(viewsets.ModelViewSet):
   queryset =  User.objects.all()
   serializer_class =  UserSerializer