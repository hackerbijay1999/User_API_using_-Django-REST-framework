from django.urls import path, include
from rest_framework import routers
from signup.views import DepartmentViewSet, OrganisationViewSet, ModulesViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'dep', DepartmentViewSet)
router.register(r'org', OrganisationViewSet)
router.register(r'mod', ModulesViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

]