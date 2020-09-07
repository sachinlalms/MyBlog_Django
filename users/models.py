from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        imag = Image.open(self.img.path)

        if imag.height > 300 or imag.width > 300:
            output_size = (300, 300)
            imag.thumbnail(output_size)
            imag.save(self.img.path)


