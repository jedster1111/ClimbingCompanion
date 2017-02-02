from rest_framework import permissions

# custom permissions to allow only the creator of climb to edit it.

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to everyone so always allow GET,HEAD,OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user