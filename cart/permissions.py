from rest_framework.permissions import BasePermission
from myprofile.models import ProfileDesigner, ProfileCustomer

class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and str(obj.user).lower() == str(request.user.email).lower())

class IsDesignerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and isinstance(request.user.profile_designer, ProfileDesigner))

class IsCustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and isinstance(request.user.profile_customer, ProfileCustomer))