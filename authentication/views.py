from rest_framework import generics, status
from .serializers import CreateUserSerializer, UsersListSerializer, UserChangeSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .utils import User, Util


class CreateUserAPIView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])
            password = Util.create_random_password()
            print(password)
            email_body = 'Ваш пароль для входа \n' + password
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Получение пароля'}
            Util.send_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all().order_by('id')
    permission_classes = (IsAdminUser,)


class UserChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserChangeSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

