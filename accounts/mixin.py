from django.contrib.auth.mixins import AccessMixin
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpRequest

class ChefRequiredMixin(AccessMixin):
    permission_denied_message = "Only Chefs are allowed to access this page. Sorry!"
    """Mixin for views that require a chef user."""
    def dispatch(self, request:HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != 'chef':
            return self.handle_no_permission(request)
        return super().dispatch(request, *args, **kwargs)
    
    def handle_no_permission(self, request) -> HttpResponseRedirect:
        messages.error(request, "Permission Denied!! Only Chefs are allowed to access this page.")
        return super().handle_no_permission()

class ClientRequiredMixin(AccessMixin):
    permission_denied_message = "Only Chefs are allowed to access this page. Sorry!"
    """Mixin for views that require a client user."""
    def dispatch(self, request:HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated or request.user.user_type != 'client':
            return self.handle_no_permission(request)
        return super().dispatch(request, *args, **kwargs)
    
    def handle_no_permission(self, request) -> HttpResponseRedirect:
        messages.error(request, "Permission Denied!! Only Clients are allowed to access this page. Sorry!")
        return super().handle_no_permission()