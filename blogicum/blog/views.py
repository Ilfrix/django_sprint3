from django.shortcuts import render


def index(request):
    template = 'blog/index.html'

    context = {'posts': posts[::-1]}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {'post': posts[0]}
    for i, d in enumerate(posts):
        if d['id'] == id:
            context = {'post': d}

    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
