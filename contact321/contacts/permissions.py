from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.owner

class OwnsRelatedContact(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.contact.owner