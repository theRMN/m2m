from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from articles.models import Article, Scope, ArticleScopeship


class ArticleScopeshipInlineFormSet(BaseInlineFormSet):
    def clean(self):
        count = 0

        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1

        if count == 0:
            raise ValidationError('У статьи должен быть основой раздел')
        if count > 1:
            raise ValidationError('Основной раздел может быть только один')

        return super().clean()


class ArticleScopeshipInline(admin.TabularInline):
    model = ArticleScopeship
    formset = ArticleScopeshipInlineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeshipInline]

