from django.shortcuts import render
from django.conf import settings

def upstream_oauth_login(request):
    template_name = getattr(settings, 'SOCIALAUTH_LOGIN_TEMPLATE_NAME', "design_system/login.html")
    return render(request, template_name, {})