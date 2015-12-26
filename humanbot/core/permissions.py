from rest_framework import permissions

from humanbot.core.models import HumanUserConnection


class UserHumanPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False

        try:
            huc = HumanUserConnection.objects.get(user=request.user,
                human_id=request.resolver_match.kwargs['human_id'])
            if request.method in permissions.SAFE_METHODS:
                return True  # read only request
            elif huc.can_write:
                return True
        except HumanUserConnection.DoesNotExist:
            pass
        return False
