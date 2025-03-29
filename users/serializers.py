from rest_framework import serializers
from .models import CustomUser, SeniorUser, JuniorUser

class CustomUserSignupSerializer(serializers.ModelSerializer):
    # Junior 전용: 범죄경력증명서 파일 입력 필드
    criminal_check_doc = serializers.FileField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password',
            'user_type', 'age', 'gender', 'region',
            'criminal_check_doc',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        doc = validated_data.pop('criminal_check_doc', None)
        password = validated_data.pop('password')

        user = CustomUser(**validated_data, user_type=user_type)
        user.set_password(password)
        user.save()

        if user_type == 'senior':
            SeniorUser.objects.create(user=user)
        elif user_type == 'junior':
            JuniorUser.objects.create(user=user, criminal_check_doc=doc)

        return user
