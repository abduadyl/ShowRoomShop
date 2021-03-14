from rest_framework.permissions import BasePermission
from myprofile.models import ProfileDesigner

class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_authenticated and str(obj.author) == str(request.user.email))

class IsDesignerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and isinstance(request.user.profile_designer, ProfileDesigner))
