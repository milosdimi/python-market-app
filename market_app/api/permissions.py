from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """Alle dürfen lesen, nur Staff/Admin darf ändern."""

    def has_permission(self, request, view):
        # SAFE_METHODS = GET, HEAD, OPTIONS (nur lesen)
        if request.method in SAFE_METHODS:
            return True
        # POST, PUT, PATCH, DELETE nur für eingeloggte Staff-User
        return bool(request.user and request.user.is_staff)
