from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.core.validators import FileExtensionValidator,MaxValueValidator, MinValueValidator

class User(AbstractUser):
    username = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    bio = models.TextField()
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'


    @classmethod
    def create_user(cls, username, email, password,):
        email = cls.objects.normalize_email(email)
        user = cls.objects.create(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return user
    
    @classmethod
    def create_super_user(cls, username, email, password, bio):
        email = cls.objects.normalize_email(email)
        user = cls.objects.create(
            username=username,
            email=email,
            bio = bio
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user
    
    def update_user(self, bio=None, image=None):
        if bio:
            self.bio = bio
        if image:
            self.image = image
        self.save()
        return self
    
    def delete_user(self):
        self.delete()

    def __str__(self):
        return self.username


class Listing(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    text = models.TextField(max_length=2400*15)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    @property
    def get_like_count(self):
        return Like.objects.filter(listing=self).count()

    @classmethod
    def create_listing(cls, title, text, user, category=None, images=None, files=None):
        listing = cls.objects.create(title=title, text=text, owner=user, category=category)

        if images:
            Image.objects.bulk_create([
                Image(listing=listing, src=image)
                for image in images
            ])

        if files:
            FileAttachment.objects.bulk_create([
                FileAttachment(listing=listing, file=file)
                for file in files
            ])

        return listing

    @classmethod
    def get_listing_by_id(cls, listing_id):
        return cls.objects.get(id=listing_id)
    
    def update_listing(self, title=None, text=None, images=None, remove_images=None, files=None, remove_files=None):
        if title:
            self.title = title
        if text:
            self.text = text
        """if category:
            self.category = category"""

        if images:
            Image.objects.bulk_create([
                Image(listing=self, src=image)
                for image in images
            ])

        if remove_images:
            for image_id in remove_images:
                try:
                    image_instance = Image.objects.get(id=image_id)
                    image_instance.delete()
                except Image.DoesNotExist:
                    pass

        if files:
            FileAttachment.objects.bulk_create([
                FileAttachment(listing=self, file=file)
                for file in files
            ])

        if remove_files:
            for file_id in remove_files:
                try:
                    file_instance = FileAttachment.objects.get(id=file_id)
                    file_instance.delete()
                except FileAttachment.DoesNotExist:
                    pass

        self.save()
        return self

    @classmethod
    def filter_listings(cls, search_param=None, owner_param=None, category_param=None):
        queryset = cls.objects.all()

        if search_param:
            queryset = queryset.filter(Q(title__icontains=search_param) | Q(text__icontains=search_param))
        if owner_param:
            queryset = queryset.filter(owner=owner_param)
        if category_param:
            queryset = queryset.filter(category=category_param)

        return queryset


    def delete_listing(self):
        self.delete()

    def __str__(self):
        return f'{self.title} - {self.owner.id}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Comment(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_comment(cls, listing, user, text):
        return cls.objects.create(listing=listing, user=user, text=text)

    def update_comment(self, text):
        self.text = text
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_for_listing(cls, listing_id):
        return cls.objects.filter(listing_id=listing_id)

    def __str__(self):
        return f'{self.user.username} - {self.listing.title}'


class Like(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    @classmethod
    def create_like(cls, user, listing):
        return cls.objects.create(user=user, listing=listing)
    
    def delete_listing(self):
        self.delete()

    @classmethod
    def user_likes_listing(cls, user, listing):
        return cls.objects.filter(user=user, listing=listing).exists()

    def __str__(self):
        return f'{self.user.username} likes {self.listing.title}'


class Image(models.Model):
    listing = models.ForeignKey('Listing', related_name='images', on_delete=models.CASCADE, validators=[FileExtensionValidator(['png'])])
    src = models.ImageField(upload_to='listing_images/', default="default.png")
    description = models.CharField(max_length=256, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FileAttachment(models.Model):
    listing = models.ForeignKey('Listing', related_name='files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='listing_attachments/')
    description = models.TextField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)