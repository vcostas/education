from django.contrib import admin
from django.contrib.auth.models import Permission
from guardian.models import GroupObjectPermission, UserObjectPermission


admin.site.register(Permission)
admin.site.register(GroupObjectPermission)
admin.site.register(UserObjectPermission)
