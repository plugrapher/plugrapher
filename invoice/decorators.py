from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def is_admin_or_staff(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def admin_or_staff_required(view_func):
    @user_passes_test(is_admin_or_staff)
    def _wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return _wrapped_view
