from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'bio', 'location', 'birth_date']
        
class RegisterSerializer(serializers.ModelSerializer):
    
    repeat_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'repeat_password']
        extra_kwargs = {
            'username': {'write_only': True},
            'email': {'write_only': True, 'required': True},
            'password': {'write_only': True},
        }
        
    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        repeat_password = self.validated_data['repeat_password']
        
        if password != repeat_password:
            raise serializers.ValidationError({"password": "Passwords must match."})
        
        user.set_password(password)
        user.save()
        
        return user            