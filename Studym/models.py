from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class fromCSV(models.Model):
    title = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to='csv/', max_length=100)
    content = models.TextField(blank=True)

    def __str_(self):
        return self.title

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    