from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class HistoryBlock(models.Model):
    id_block = models.AutoField(primary_key=True)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return str(self.id_block)

class HistoryElement(models.Model):

    id_element = models.AutoField(primary_key=True)
    id_block = models.ForeignKey(HistoryBlock, to_field='id_block', on_delete=models.CASCADE)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    title = models.CharField(max_length=200, default=None, null=True, blank=True)
    text = models.TextField(max_length=65535, default=None, null=True, blank=True)
    
    title_list = models.CharField(max_length=100, default=None, null=True, blank=True)
    text_list = models.TextField(max_length=65535, default=None, null=True, blank=True)

    title_img = models.CharField(max_length=100, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id_element)


class HistoryImage(models.Model):

    id_element = models.ForeignKey(HistoryElement, to_field='id_element', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='images/about/history')





class StructureBlock(models.Model):

    id_block = models.AutoField(primary_key=True)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    type_block = models.IntegerField(default=1) 
    #first type - fix size block
    #second type - filling size

    def __str__(self):
        return str(self.id_block)

class StructureElement(models.Model):
    id_element = models.AutoField(primary_key=True)
    id_block = models.ForeignKey(StructureBlock, to_field='id_block', on_delete=models.CASCADE)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    title_h = models.CharField(max_length=200, default=None, null=True, blank=True)
    title_l = models.CharField(max_length=200, default=None, null=True, blank=True)

    text = models.TextField(max_length=65535, default=None, null=True, blank=True)

    list_title = models.CharField(max_length=100, default=None, null=True, blank=True)

    quote = models.CharField(max_length=400, default=None, null=True, blank=True)
    quote_author = models.CharField(max_length=400, default=None, null=True, blank=True)

    contact_post = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_name = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_phone = models.CharField(max_length=400, default=None, null=True, blank=True)
    contact_email = models.CharField(max_length=400, default=None, null=True, blank=True)

    img_title = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id_element)

class StructureImage(models.Model):
    id_element = models.ForeignKey(StructureElement, to_field='id_element', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/structure/history')

class StructureList(models.Model):
    id_element = models.ForeignKey(StructureElement, to_field='id_element', on_delete=models.CASCADE)
    list_element = models.CharField(max_length=400, default=None, null=True, blank=True)