from rest_framework import permissions


class IsStaffEditorPermission(
    permissions.DjangoModelPermissions
):  # See this is How we create permissions
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    #  This is  basically a logic to create Permissions
    # def has_permission(self, request, view):
    #     user = request.user
    #     # print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm(
    #             "products.view_product"
    #         ):  # The syntax to create permission is "app_name.verb_model_name"
    #             print(user.get_all_permissions())
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         return False
    #     return False
