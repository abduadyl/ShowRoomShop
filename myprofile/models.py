from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from myprofile.utils import get_random_code


MyUser = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=300, default='no bio...')
    avatar = models.ImageField(upload_to='avatars/', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return f'{self.user.email}'

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + ' ' + str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + ' ' + str(get_random_code()))
                ex = Profile.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)
