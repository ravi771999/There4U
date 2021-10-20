from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from user_api.models import User
from user_api.serializers import UserSerializer,PasswordSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def recent_users(self, request):
        recent_users = User.objects.all().order('-last_login')
        page = self.paginate_queryset(recent_users)
        serializer = self.get_pagination_serializer(page)
        return Response(serializer.data)

