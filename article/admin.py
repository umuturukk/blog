from django.contrib import admin
from .models import Article

# Register your models here.
# Oluşturmuş olduğumuz modelleri burada admin paneline belli fonksiyonlar aracılığıyla kayıt ediyoruz.
admin.site.register(Article)
