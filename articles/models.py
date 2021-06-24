from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.TextField()
    tag = models.ManyToManyField(Article, through='ArticleScopeship', related_name='scopes')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class ArticleScopeship(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        default=None,
        related_name='scopeships',
    )
    scope = models.ForeignKey(
        Scope,
        on_delete=models.CASCADE,
        default=None,
        related_name='scopeships',
        verbose_name='Разделы')

    is_main = models.BooleanField(
        verbose_name='основной'
    )

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self):
        return f'id:({self.id}) == {str(self.is_main)}'
