# ls listings_app/tests.py | entr -pc python manage.py test
# coverage run --source="." manage.py test
# coverage report -m
from django.test import TestCase
from .models import Listing, User, Category, Comment, Like, Image, FileAttachment


class ListingTestCase(TestCase):

    def setUp(self):
        user = User.create_user(
            username='test_user',
            email='new@example.com',
            password='password')
        category = Category.objects.create(name='test_category')
        images = [
            'test_files/image1.jpg',
            'test_files/image2.jpg',
            'test_files/image3.png',
            'test_files/image4.jpg',
            'test_files/image5jpg']
        files = ['test_files/file1.txt', 'test_files/file2.pdf']
        listing = Listing.create_listing(
            title='Test Listing',
            text='This is a test listing.',
            user=user,
            category=category,
            images=images,
            files=files)
        Comment.create_comment(
            listing=listing,
            user=user,
            text='This is a test comment.')
        Like.create_like(user=user, listing=listing)

    def test_listing_creation(self):
        listing = Listing.objects.get(id=1)
        self.assertEqual(listing.title, 'Test Listing')
        self.assertEqual(listing.text, 'This is a test listing.')

        images_exist = Image.objects.filter(listing=listing).exists()
        self.assertTrue(images_exist, "Images do not exist for the listing")

        files_exist = FileAttachment.objects.filter(listing=listing).exists()
        self.assertTrue(files_exist, "Files do not exist for the listing")

    def test_update_listing(self):
        listing = Listing.objects.get(id=1)
        new_images = ['test_files/image6.jpg', 'test_files/image7.gif']
        new_files = ['test_files/file2.pdf']
        remove_images = [1, 2, 3]
        remove_files = [1]

        listing.update_listing(
            images=new_images,
            remove_images=remove_images,
            files=new_files,
            remove_files=remove_files)

        for image in new_images:
            self.assertTrue(listing.images.filter(src=image).exists())

        for file in new_files:
            self.assertTrue(listing.files.filter(file=file).exists())

        for image_id in remove_images:
            self.assertFalse(listing.images.filter(id=image_id).exists())

        for file_id in remove_files:
            self.assertFalse(listing.files.filter(id=file_id).exists())

    def test_delete_listing(self):
        listing = Listing.objects.get(id=1)
        listing.delete_listing()
        with self.assertRaises(Listing.DoesNotExist):
            Listing.objects.get(id=1)

    def test_filter_listings(self):
        filtered_listings = Listing.filter_listings(search_param='Test')
        self.assertEqual(filtered_listings.count(), 1)

        user = User.create_user(
            username='test_user2',
            email='test2@example.com',
            password='testing_password')
        category = Category.objects.create(name='another_category')
        Listing.objects.create(
            title='Another Test Listing',
            text='This is another test listing.',
            owner=user,
            category=category)

        filtered_listings = Listing.filter_listings(
            search_param='Test', owner_param=user, category_param=category)
        self.assertEqual(filtered_listings.count(), 1)

        filtered_listings = Listing.filter_listings(
            search_param='Test', owner_param=user)
        self.assertEqual(filtered_listings.count(), 1)

        filtered_listings = Listing.filter_listings(category_param=category)
        self.assertEqual(filtered_listings.count(), 1)

        filtered_listings = Listing.filter_listings(owner_param=user)
        self.assertEqual(filtered_listings.count(), 1)

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.text, 'This is a test comment.')

    def test_update_comment(self):
        comment = Comment.objects.get(id=1)
        comment.update_comment(text='Updated comment text.')
        updated_comment = Comment.objects.get(id=1)
        self.assertEqual(updated_comment.text, 'Updated comment text.')

    def test_delete_comment(self):
        comment = Comment.objects.get(id=1)
        comment.delete_comment()
        with self.assertRaises(Comment.DoesNotExist):
            Comment.objects.get(id=1)

    def test_get_comments_for_listing(self):
        listing = Listing.objects.get(id=1)
        Comment.objects.create(
            listing=listing, user=User.objects.get(
                id=1), text='Another comment.')
        comments = Comment.get_comments_for_listing(listing_id=1)
        self.assertEqual(comments.count(), 2)

    def test_like_creation(self):
        like = Like.objects.get(id=1)
        self.assertEqual(like.user.username, 'test_user')
        self.assertEqual(like.listing.title, 'Test Listing')

    def test_user_likes_listing(self):
        user = User.objects.get(username='test_user')
        listing = Listing.objects.get(title='Test Listing')
        self.assertTrue(Like.user_likes_listing(user=user, listing=listing))

    def test_delete_like(self):
        like = Like.objects.get(id=1)
        like.delete()
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=1)

    def test_create_user_method(self):
        user = User.create_user(
            username='new_user',
            email='test@example.com',
            password='password')
        self.assertEqual(user.username, 'new_user')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password'))

    def test_create_super_user_method(self):
        user = User.create_super_user(
            username='super_user',
            email='super@example.com',
            password='password',
            bio='Super bio')
        self.assertEqual(user.username, 'super_user')
        self.assertEqual(user.email, 'super@example.com')
        self.assertEqual(user.bio, 'Super bio')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password('password'))

    def test_update_user_method(self):
        user = User.objects.get(id=1)
        user.update_user(bio='Updated bio')
        updated_user = User.objects.get(id=1)
        self.assertEqual(updated_user.bio, 'Updated bio')

    def test_delete_user_method(self):
        user = User.objects.get(id=1)
        user.delete_user()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=1)
