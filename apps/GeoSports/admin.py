from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from apps.GeoSports.models import Profile

from django.utils.translation import ugettext_lazy as _


class ProfilesInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = _('Profiles')


class UserAdmin(BaseUserAdmin):
    inlines = (ProfilesInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
