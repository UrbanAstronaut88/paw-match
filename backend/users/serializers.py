from typing import Any

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework import serializers

from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )
    password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    surname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    city = serializers.CharField(required=False, allow_blank=True, max_length=100)
    birthday = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "password2",
            "name",
            "surname",
            "city",
            "birthday",
        )

    def validate_email(self, email: str) -> str:
        normalized_email: str = email.strip().lower()

        if User.objects.filter(email=normalized_email).exists():
            raise serializers.ValidationError(
                "User with this email already exists"
            )

        return normalized_email

    def validate_birthday(self, birthday: Any) -> Any:
        if birthday and birthday > timezone.now().date():
            raise serializers.ValidationError("Birthday cannot be in the future.")

        return birthday

    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")

        validate_password(data["password"])
        return data

    def create(self, validated_data: dict[str, Any]) -> User:
        name: str = validated_data.pop("name", "").strip()
        surname: str = validated_data.pop("surname", "").strip()
        city: str = validated_data.pop("city", "").strip()
        birthday = validated_data.pop("birthday", None)
        validated_data.pop("password2")

        email: str = validated_data["email"]

        user: User = User.objects.create_user(
            username=email,
            email=email,
            password=validated_data["password"],
        )

        profile: UserProfile = user.profile
        profile.name = name
        profile.surname = surname
        profile.city = city
        profile.birthday = birthday
        profile.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )

    def validate(self, data: dict[str, Any]) -> dict[str, Any]:
        email: str = data["email"].strip().lower()

        user: User | None = User.objects.filter(email=email).first()

        if user is None:
            raise serializers.ValidationError({"email": "User not found"})

        authenticated_user: User | None = authenticate(
            username=user.username,
            password=data["password"]
        )

        if authenticated_user is None:
            raise serializers.ValidationError({"password": "Invalid credentials"})

        data["user"] = authenticated_user
        return data


class UserProfileReadSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ("name", "surname", "city", "birthday", "avatar")


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    surname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    city = serializers.CharField(required=False, allow_blank=True, max_length=100)
    birthday = serializers.DateField(required=False, allow_null=True)
    avatar = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = UserProfile
        fields = ("name", "surname", "city", "birthday", "avatar")

    def validate_name(self, value: str) -> str:
        return value.strip()

    def validate_surname(self, value: str) -> str:
        return value.strip()

    def validate_city(self, value: str) -> str:
        return value.strip()

    def validate_birthday(self, birthday: Any) -> Any:
        if birthday and birthday > timezone.now().date():
            raise serializers.ValidationError("Birthday cannot be in the future.")

        return birthday

    def validate_avatar(self, value: Any) -> Any:
        max_size_in_bytes: int = 5 * 1024 * 1024

        if hasattr(value, "size") and value.size > max_size_in_bytes:
            raise serializers.ValidationError(
                "Avatar file is too large. Maximum size is 5 MB."
            )

        if hasattr(value, "content_type") and not value.content_type.startswith("image/"):
            raise serializers.ValidationError(
                "Only image files are allowed."
            )

        return value


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileReadSerializer(read_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "profile")


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )
    new_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )
    new_password2 = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        request = self.context["request"]
        user: User = request.user

        old_password: str = attrs["old_password"]
        new_password: str = attrs["new_password"]
        new_password2: str = attrs["new_password2"]

        if not user.check_password(old_password):
            raise serializers.ValidationError(
                {"old_password": "Old password is incorrect."}
            )

        if new_password != new_password2:
            raise serializers.ValidationError(
                {"new_password2": "Passwords do not match."}
            )

        validate_password(new_password, user=user)

        if old_password == new_password:
            raise serializers.ValidationError(
                {"new_password": "New password must be different from old password."}
            )

        return attrs
