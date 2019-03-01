from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate
import base64


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2 and auth[0].lower() == "basic":
            byte_value = base64.b64decode(auth[1])
            username, password = byte_value.decode('ascii').split(':')
            user = authenticate(username=username, password=password)
            if user:
                return user, None
        raise exceptions.AuthenticationFailed('Unauthorized user')

