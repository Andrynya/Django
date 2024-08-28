from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_content = models.CharField('Краткое содержание', max_length=200)
    content = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    publikator = models.CharField('Автор', max_length=30)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title