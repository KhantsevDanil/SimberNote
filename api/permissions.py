from rest_framework import permissions, status
from rest_framework.exceptions import APIException


class AnonForbidden(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserForbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (obj.author == request.user
                or request.user.is_moderator
                or request.user.is_admin)

class ReadOnlyOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user.is_moderator
                or request.user.is_admin)