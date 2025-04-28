from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

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
    service_href = models.CharField(max_length=500, default="local", blank=True, null=True)
    def __str__(self):
        return str(self.id) + ". " + str(self.service)

class ServiceElement(models.Model):
    main_page_service_list_fk = models.ForeignKey(MainPageServiceList, on_delete=models.CASCADE)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    title = models.CharField(max_length=200, default=None, null=True, blank=True)
    
    text = models.TextField(max_length=65535, default=None, null=True, blank=True)

    contact_title = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_phone = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_form = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_form_href = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_email = models.CharField(max_length=400, default=None, null=True, blank=True)

    list_title = models.CharField(max_length=100, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.main_page_service_list_fk)
    
class ServiceList(models.Model):
    id_element = models.ForeignKey(ServiceElement, on_delete=models.CASCADE)
    list_element = models.CharField(max_length=400, default=None, null=True, blank=True)
 

class RuleTitle(models.Model):
    title = models.CharField(max_length=200, default=None, null=True, blank=True)
    text_title = models.CharField(max_length=600, default=None, null=True, blank=True)
    optional_text_title = models.CharField(max_length=600, default=None, null=True, blank=True)


class RuleBlock(models.Model):
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    def __str__(self):
        return str(self.priority)
    

class RuleElement(models.Model):
    id_block = models.ForeignKey(RuleBlock, on_delete=models.CASCADE)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    title = models.CharField(max_length=200, default=None, null=True, blank=True)

    text = models.TextField(max_length=65535, default=None, null=True, blank=True)

class RuleElementList(models.Model):
    id_element = models.ForeignKey(RuleElement, on_delete=models.CASCADE)
    list_element = models.CharField(max_length=1000, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id_element)
