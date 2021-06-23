from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from articles.models import Article, Scope, ArticleScopeship


class ArticleScopeshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            form.cleaned_data
            raise ValidationError('Тут всегда ошибка')
        return super().clean()


class ArticleScopeshipInline(admin.TabularInline):
    model = ArticleScopeship


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeshipInline]
