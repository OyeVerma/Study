import json
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
    
    
class Topic(models.Model):
    title = models.CharField(unique=True, max_length=50)
    text = models.TextField()
    slug = models.SlugField(editable=False)
    def __str__(self):
        return slugify(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def getTextList(self):
        d = []
        lines = self.text.split('\n')
        cwlist = []
        for line in lines:
            if line != '':
                if line[:2] == '--':
                    cwlist.append(line[2:])
                elif line[0] == '-':
                    if len(cwlist) != 0:
                        d.append(cwlist)
                        cwlist = []
                    cwlist.append(line[1:])
        d.append(cwlist)
        return d
