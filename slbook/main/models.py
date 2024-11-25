from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    article_text = models.CharField(max_length=1000, null=True, default=None)
    image = models.ImageField(null=True)
    
    def __str__(self):
        return self.title