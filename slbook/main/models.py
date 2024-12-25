from django.db import models

class Setting(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name variable')
    count_news_on_page = models.PositiveSmallIntegerField('Variable value')
    def __str__(self):
        return self.title
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    article_text = models.CharField(max_length=1000, null=True, default=None)
    image = models.ImageField(null=True, upload_to='images/')
    date_new = models.DateTimeField(null=True)

    def __str__(self):
        return self.title