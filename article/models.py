from django.db import models

# Create your models here.

# Article modelini, models içindeki Model class'ından türetiyoruz.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE) # auth.User tablosundan bir foreign key belirledik(tabloları ilişkilendirdik.) 
    #on_delete parametresi ile kullanıcı silindiğinde ona ait makalelerin de silinmesine dair belirleme yaptık.
    title = models.CharField(max_length = 50) # başlık alanını uzunluğu maksimum 50 karakter olacak şekilde oluşturduk.
    content = models.TextField() # içerik alanını oluşturduk.
    created_date = models.DateTimeField(auto_now_add = True) # makalenin oluşturulma tarihini o anın tarihine göre atayacak şekilde oluşturduk.
    



