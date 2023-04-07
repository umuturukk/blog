from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Article modelini, models içindeki Model class'ından türetiyoruz.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = 'Yazar') # auth.User tablosundan bir foreign key belirledik(tabloları ilişkilendirdik.) 
    #on_delete parametresi ile kullanıcı silindiğinde ona ait makalelerin de silinmesine dair belirleme yaptık.
    title = models.CharField(max_length = 50, verbose_name = 'Başlik') # başlık alanını uzunluğu maksimum 50 karakter olacak şekilde oluşturduk.
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Oluşturulma Tarihi') # makalenin oluşturulma tarihini o anın tarihine göre atayacak şekilde oluşturduk.
    article_image = models.FileField(blank = True, null = True, verbose_name = "Makaleye Fotoğraf Ekleyin")
    # article object yerine, o makalenin başlığı gözükücek.
    
    def __str__(self):
        return self.title
    


