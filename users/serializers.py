from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import ContentType#, Permission
from .models import Role, User, Permission

# User = get_user_model()


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class ContentTypeRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return ContentTypeSerializer(value).data

    def to_internal_value(self, data):
        return data


class PermissionSerializer(serializers.ModelSerializer):
    # codename = serializers.CharField(max_length=100, write_only=True)
    # content_type = ContentTypeRelatedField(many=True)
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return PermissionSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoleSerializer(serializers.ModelSerializer):
    permissions = PermissionRelatedField(many=True)

    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):
        permissions = validated_data.pop('permissions', None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.permissions.add(*permissions)
        instance.save()
        return instance


class RoleRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return RoleSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=250, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):  # type: ignore
        """Get user token."""
        user = User.objects.get(username=obj)

        return {'refresh': user.tokens['refresh'], 'access': user.tokens['access']}

    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']

    def validate(self, data):  # type: ignore
        """Validate and return user login."""
        username = data['username']
        password = data['password']
        if username is None:
            raise serializers.ValidationError('An email address is required to log in.')

        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        return user


class LogoutSerializer(serializers.Serializer[User]):
    refresh = serializers.CharField()

    def validate(self, attrs):  # type: ignore
        """Validate token."""

        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):  # type: ignore
        """Validate save backlisted token."""

        try:
            RefreshToken(self.token).blacklist()
        except TokenError as ex:
            raise exceptions.AuthenticationFailed(ex)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Enter password', write_only=True, required=True, max_length=200)
    password_confirm = serializers.CharField(label='Repeat password', write_only=True, required=True, max_length=200)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'password', 'password_confirm', 'role',
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'password_confirm': {'write_only': True},
        # }

    def validate_password2(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            msg = 'Passwords do not match!'
            raise ValidationError(msg)
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=True,
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    # role = RoleRelatedField(many=False, queryset=Role.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'measurer', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
