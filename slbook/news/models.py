from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

POSITION = (
    ('L', 'Left'),
    ('R', 'Right')
)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    article_text = models.TextField(max_length=2500, null=True, default=None)
    image = models.ImageField(null=True, upload_to='images/')
    image_position = models.CharField(max_length=1, choices=POSITION, default='L')
    date_new = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
