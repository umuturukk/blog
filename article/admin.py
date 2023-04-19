from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# Oluşturmuş olduğumuz modelleri burada admin paneline belli fonksiyonlar aracılığıyla kayıt ediyoruz.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_date'] # Article başlığı, article yazarı ve oluşturulma tarihi gösterildi.
    list_display_links = ['title', 'created_date'] # Başlık ve oluşturulma tarihine tıklayarak bir sonraki sayfaya geçebiliyoruz.
    search_fields = ['title'] # başlık ve yazar bilgisine göre arama özelliği kazandırdık.
    list_filter = ['created_date'] # Oluşturulma tarihi filtresine göre seçtiğimiz tarihte oluşturulan makaleleri seçebileceğiz.

    # Bu bize djangonun söylediği bir şey.
    class Meta:
        model = Article
