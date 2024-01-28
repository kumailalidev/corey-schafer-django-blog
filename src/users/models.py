from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    def upload_to(self, filename):
        return f"users/{self.user.username}/pictures/{filename}"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to=upload_to, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # only if image is uploaded
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
