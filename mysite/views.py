from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserInfoViewSet(viewsets.ViewSet):
    """
    Displays the user's info
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is 'me' then return the current user.
        """
        if request.user and pk == 'me':
            qs = self.queryset.get(pk=request.user.id)
            return Response(
                UserSerializer(qs, context={'request': request}).data
            )
        raise ParseError()
