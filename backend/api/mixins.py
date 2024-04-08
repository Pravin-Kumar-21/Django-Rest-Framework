""" now we have created a mixin class for permission 
 we can jus use it any of the classes of views .py file 
 by just using this class now we need not to declare a permission every time
 """

from .permissions import IsStaffEditorPermission
from rest_framework import permissions


class StaffEditorPermissionsMixin:
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
