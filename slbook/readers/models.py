from django.db import models

class MainPageService(models.Model):
    main_title = models.CharField(max_length=200)
    top_title = models.CharField(max_length=200)

    main_text = models.TextField(max_length=4000)
    list_title = models.CharField(max_length=200)

    def __str__(self):
        return self.main_title

class MainPageServiceList(models.Model):
    main_page_fk = models.ForeignKey(MainPageService, on_delete=models.CASCADE)
    service = models.CharField(max_length=200)