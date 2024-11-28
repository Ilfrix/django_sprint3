from django.shortcuts import render, get_object_or_404, get_list_or_404
from blog.models import Post, Category
from django.db.models import Q
from datetime import datetime as dt


def index(request):
    template = 'blog/index.html'
    
    posts = Post.objects.all().filter(
        Q(is_published=True)
        & Q(category__is_published=True)
        & Q(pub_date__lte=dt.now())
    ).order_by('pub_date').reverse()[:5]
    print(posts)
    #     is_published=True,
    # category__is_published=True
    # Q(pub_date>=dt.now())
    # .order_by('created_at').reverse()[:5]

    # context = {'posts': posts[::-1]}
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    posts = get_object_or_404(Post.objects.all().filter(
        Q(is_published=True)
        & Q(category__is_published=True)
        & Q(pub_date__lte=dt.now())
    ), pk=id)
    context = {
        'post': posts
    }

    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_list_or_404(
        Post.objects.all().filter(
            category__slug=category_slug,

            pub_date__lte=dt.now(),
            is_published=True
        ),
        category__is_published=True
    )
    context = {
        'category': category_slug,
        'post_list': category
    }
    return render(request, template, context)
