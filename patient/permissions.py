from rest_framework.permissions import BasePermission


class IsDoctorPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated: #check if user is authenticated
            return False

        # check if user is doctor
        return request.user.is_doctor