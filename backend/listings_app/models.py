from django.db import models, transaction
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def create_user(sender, instance, created, **kwargs):
        if created:
            User.objects.create(user=instance)


def save_user(sender, instance, **kwargs):
    instance.create(user=instance)

    """ def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(create_user_profile, sender=User)
    post_save.connect(save_user_profile, sender=User) """


class Listing(models.Model):
    title = models.CharField(max_length=256, db_index=True)
    text = models.TextField()
    rank = models.IntegerField(db_index=True)

    class Meta:
        ordering = ['rank']

    def __str__(self):
        return f'{self.rank} - {self.pk} - {self.title} - {self.text}'

    @classmethod
    def create(cls, title=title, text=text):
        cls.objects.create(
            title=title,
            text=text,
            rank=cls.highest_rank + 1
        )

    @classmethod
    @property
    def highest_rank(cls):
        return int(cls.objects.all().aggregate(models.Max('rank'))['rank__max'] or 0)

    def rerank(self, new_rank):
        with transaction.atomic():
            if self.rank == new_rank:
                return
            elif new_rank < self.rank:
                delta = 1
                listings = type(self).objects.filter(
                    rank__gte=new_rank).filter(rank__lte=self.rank)
            else:
                delta = -1
                listings = type(self).objects.filter(
                    rank__gte=self.rank).filter(rank__lte=new_rank)
            for listing in listings:
                if listing.rank == self.rank:
                    listing.rank = new_rank
                else:
                    listing.rank += delta
            type(self).objects.bulk_update(listings, fields=('rank',))

    @classmethod
    def rerank_by_list(cls, reranked):
        listings = [listing.pk for listing in cls.objects.all()]

        for i, samples in enumerate(zip(listings, reranked)):
            if not samples[0] == samples[1]:
                new_i_index = reranked.index(listings[i])
                if new_i_index > i + 1:
                    cls.objects.get(pk=listings[i]).rerank(new_i_index + 1)
                else:
                    cls.objects.get(pk=reranked[i]).rerank(new_i_index)
                break

    def delete(self, *args, **kwargs):
        self.rerank(type(self).highest_rank)
        super(type(self), self).delete(*args, **kwargs)
