from django.shortcuts import render
from articles.models import Article
import operator


def articles_list(request):
    template = 'articles/news.html'

    article = Article.objects.order_by('-published_at').all().prefetch_related('scopes', 'scopeships').defer('id')

    object_list = []

    count = 0

    for ar in article:
        obj = {
            'title': ar.title,
            'text': ar.text,
            'published_at': ar.published_at,
            'image': ar.image,
            'scopes': {
                'all': [
                ]
            }
        }

        for i in ar.scopeships.order_by('-scope_id').all():
            tag = ar.scopes.order_by('-id', 'name').all()[count]

            if i.scope_id == tag.id:
                obj['scopes']['all'].append({'is_main': i.is_main, 'tag': {'name': tag.name}})

                if count < (len(ar.scopes.all()) - 1):
                    count += 1
                else:
                    count = 0

        obj['scopes']['all'].sort(key=operator.itemgetter('is_main'), reverse=True)

        object_list.append(obj)

    context = {
        'object_list': object_list
    }

    return render(request, template, context)
