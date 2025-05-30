from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Здесь описаны таблицы для динамического отображения статики сайта 
# 
# Вся динамика состоит из белых блоков и элементов внутри
# И блок и элемент имеет приоритет относительно других блоков и элементов соответсвенно 
# 
# На каждую статическую страницу имеется минимум ДВЕ обязательные таблицы
#   1) Таблица блоков (*Block)
#   2) Таблица елементов (*Element)
#  




# Сайт с историей библиотеки содержит 3 таблицы - 2 обязательные и 1 вспомогательная с картинками


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



# Сайт со структурой библиотеки содержит 4 таблицы - 2 обязательные и 2 вспомогательные:
#   1) Вспомогательная таблица с картинками
#   2) Вспомогательная таблица со списком

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
    image = models.ImageField(upload_to='images/about/structure')

class StructureList(models.Model):
    id_element = models.ForeignKey(StructureElement, to_field='id_element', on_delete=models.CASCADE)
    list_element = models.CharField(max_length=400, default=None, null=True, blank=True)


# Сайт с партёрами библиотеки содержит 5 таблиц - 2 обязательные и 3 вспомогательные:
#   1) Вспомогательная таблица с картинками
#   2) Вспомогательная таблица со списком
#   3) Вспомогательная таблица с автором цитаты


class PartnershipBlock(models.Model):
    id_block = models.AutoField(primary_key=True)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return str(self.id_block)

class PartnershipElement(models.Model):
    id_element = models.AutoField(primary_key=True)
    id_block = models.ForeignKey(PartnershipBlock, to_field='id_block', on_delete=models.CASCADE)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    title = models.CharField(max_length=200, default=None, null=True, blank=True)

    text = models.TextField(max_length=65535, default=None, null=True, blank=True)

    img_title = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return str(self.id_element)

class PartnershipImage(models.Model):
    id_element = models.ForeignKey(PartnershipElement, to_field='id_element', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/about/partnership')
 
class PartnershipList(models.Model):
    id_element = models.ForeignKey(PartnershipElement, to_field='id_element', on_delete=models.CASCADE)
    list_element = models.CharField(max_length=400, default=None, null=True, blank=True)

class PartnershipAuthor(models.Model):
    id_element = models.ForeignKey(PartnershipElement, to_field='id_element', on_delete=models.CASCADE)
    author_paragraph = models.CharField(max_length=400, default=None, null=True, blank=True)


# Сайт с официальными документами состоит из двух таблиц 
#   1) Таблица с блоками
#   2) Вспомогательная таблица с файлами


class FileBlock(models.Model):
    id_block = models.AutoField(primary_key=True)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return str(self.id_block)

class FileElement(models.Model):
    id_block = models.ForeignKey(FileBlock, to_field='id_block', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=400, default=None, null=True, blank=True)
    file = models.FileField(upload_to='files/about/official')

    def __str__(self):
        return str(self.id)




class BiblioMassMedia(models.Model):
    name_new = models.CharField(max_length=500, default=None, null=True, blank=True)
    priority = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    image_new = models.ImageField(upload_to='images/about/media', null=True, blank=True)
    href_new = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.name_new