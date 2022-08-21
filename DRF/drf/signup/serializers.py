from rest_framework import serializers
from signup.models import Department, Organisation, Modules, User

class DepartmentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Department
       fields = ('dept_name', 'org_name')


class OrganisationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Organisation
       fields = ('org_name', 'logo')


class ModulesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Modules
       fields = ('mod_name',)


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('first_name', 'last_name', 'user_name', 'dept_name', 'org_name', 'designation', 'role', 'modules', 'email', 'phone', 'password')



