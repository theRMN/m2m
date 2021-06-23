from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scope = models.ForeignKey('Scopes', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scopes(models.Model):
    name = models.TextField()


class Tags(models.Model):
    name = models.TextField()
    scopes = models.ManyToManyField(Scopes, related_name='tag')




