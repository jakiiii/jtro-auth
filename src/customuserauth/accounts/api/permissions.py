from rest_framework import permissions


class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        pass
        # ip_addr = request.META['REMOTE_ADDR']
        # blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        # return not blacklisted


class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticate user. Please log out to try again.'
    """
    Non authenticated user permission.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You must be the owner of this content.'
    """
        Object-level permission to only allow owners of an object to edit it.
        Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user
