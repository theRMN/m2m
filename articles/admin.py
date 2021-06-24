from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from articles.models import Article, Scope, ArticleScopeship


# class ArticleScopeshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         count = 0
#         has_tag = False
#
#         for form in self.forms:
#             if form.cleaned_data.get('is_main'):
#                 count += 1
#             if form.cleaned_data.get('scope'):
#                 has_tag = True
#
#         if count == 0 and has_tag:
#             raise ValidationError('Тут всегда ошибка')
#         if count > 1:
#             raise ValidationError('Тут всегда ошибка')
#
#         return super().clean()

# Оно просто не работает.....................................


class ArticleScopeshipInline(admin.TabularInline):
    model = ArticleScopeship


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeshipInline]

