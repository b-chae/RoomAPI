import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms=['hS256'])

            pk = decoded.get("id")
            user = User.objects.get(pk=pk)
            return (user, None)
        except ValueError:
            return None
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(detail="JWT Format Invalid")
