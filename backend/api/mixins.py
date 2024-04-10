""" now we have created a mixin class for permission 
 we can jus use it any of the classes of views .py file 
 by just using this class now we need not to declare a permission every time
 """

from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditorPermissionsMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetmixin:
    user_field = "user"
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and self.request.user.is_staff:
            return qs
        return qs.filter(**lookup_data)
