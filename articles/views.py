from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    article = Article.objects.order_by('-published_at').all()

    object_list = []

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
        print(ar.scopes.all())
        for i in ar.scopes.all():
            obj['scopes']['all'].append({'tag': {'name': i.name}})

        object_list.append(obj)

    context = {
        'object_list': object_list
    }

    return render(request, template, context)
