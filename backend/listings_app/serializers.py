from rest_framework import serializers
from .models import Listing, User, Image, Category, Comment, Like, FileAttachment
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from html_sanitizer import Sanitizer
from django.core.validators import MaxValueValidator, MinValueValidator


def validate_field(value, min_length, max_length, field_name):
    sanitizer = Sanitizer()
    sanitized_text = sanitizer.sanitize(value)

    if len(value) < min_length or len(value) > max_length:
        raise serializers.ValidationError({field_name: f'{field_name} Must be between {min_length} and {max_length} characters long.'})

    return sanitized_text

class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(min_length=1, max_length=50)
    bio = serializers.CharField(min_length=1, max_length=600, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2', 'image', 'bio')
        

    def validate(self, attrs):
        instance = self.instance
        if instance is None:
            existing_user = User.objects.filter(username__iexact=attrs['username']).exists()
            if existing_user:
                raise serializers.ValidationError(
                    {"username": "A user with this username already exists."})

            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError(
                    {"password": "Password fields didn't match."})
        else:
            pass

        return attrs

    def create(self, validated_data):
        user = User.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    

    def update(self, instance, validated_data):
        bio = validated_data.get('bio')
        image = validated_data.get('image')
        instance.update_user(bio=bio, image=image)
        return instance


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    text = serializers.CharField(min_length=1, max_length=5000)

    def create(self, validated_data):
        comment = Comment.create_comment(**validated_data)
        return comment
    
    def update(self, instance, validated_data):
        instance.update_comment(**validated_data)
        return instance

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'listing': {'required': False, 'allow_null': True}}



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FileAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAttachment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

from django.core.validators import MaxValueValidator, MinValueValidator

class ListingSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = ImageSerializer(many=True, required=False)
    files = FileAttachmentSerializer(many=True, required=False)
    like_count = serializers.SerializerMethodField()
    text = serializers.CharField(min_length=4, max_length=(15*2400))

    class Meta:
        model = Listing
        fields = '__all__'

    
    def get_like_count(self, obj):
        return obj.get_like_count
    
    def validate(self, attrs):
        print(attrs)
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('is_featured', None)
        listing = Listing.create_listing(**validated_data)
        return listing
    
    def update(self, instance, validated_data):
        print(validated_data)
        validated_data.pop('is_featured', None)
        listing = Listing.update_listing(instance, **validated_data)
        return listing