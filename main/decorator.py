from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect


def superuser_only(function):
    def _inner(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect('/')
        return function(request, *args, **kwargs)
    return _inner