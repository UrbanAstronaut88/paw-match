from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer,
    RegisterSerializer,
    UserProfileReadSerializer,
    UserProfileUpdateSerializer,
    UserSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer: RegisterSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = serializer.save()

        response_serializer: UserSerializer = UserSerializer(user)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request: Request) -> Response:
        serializer: LoginSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: User = serializer.validated_data["user"]
        refresh: RefreshToken = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            },
            status=status.HTTP_200_OK
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: None},
        description="Logout current user on client side by removing JWT tokens"
    )
    def post(self, request: Request) -> Response:
        return Response(
            {"message": "Successfully logged out"},
            status=status.HTTP_200_OK
        )


class MeView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @extend_schema(
        responses=UserSerializer,
        description="Get current authenticated user with profile"
    )
    def get(self, request: Request) -> Response:
        serializer: UserSerializer = UserSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        request=UserProfileUpdateSerializer,
        responses=UserProfileReadSerializer,
        description="Update current user profile"
    )
    def patch(self, request: Request) -> Response:
        profile = request.user.profile

        serializer: UserProfileUpdateSerializer = UserProfileUpdateSerializer(
            profile,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_serializer: UserProfileReadSerializer = UserProfileReadSerializer(profile)
        return Response(response_serializer.data)


class ChangePasswordView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    @extend_schema(
        request=ChangePasswordSerializer,
        responses={200: None},
        description="Change password for current authenticated user"
    )
    def patch(self, request: Request) -> Response:
        serializer: ChangePasswordSerializer = self.get_serializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user: User = request.user
        new_password: str = serializer.validated_data["new_password"]

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Password changed successfully."},
            status=status.HTTP_200_OK
        )
