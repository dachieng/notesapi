from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, min_length=6)
    username = serializers.CharField(min_length=3)
    password = serializers.CharField(max_length = 250, min_length=6, write_only = True)

    def validate(self, attrs):
        username = attrs.get("username", '')
        email = attrs.get("email", '')
        password = attrs.get("password", '')
      

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email_error':'Email already exists'})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username_error":'Username already exists'})
        
       

        return super().validate(attrs)
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password']) # hash the password
        #user.set_password(validated_data['password2'])
        user.save()
        return user

    class Meta:
        model = User

        fields = ['username', 'email', 'password']

        
