import requests
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Post, Contact, Comment

BOT_TOKEN = '6787403849:AAE2piymBY7F-9DCRKbEK3kZoBx1paVSTog'
CHAT_ID = '654348985'


def home_view(request):
    posts = Post.objects.filter(is_published=True).order_by('-views_count')[:2]

    d = {
        'posts': posts,
        'home': 'active'
    }

    return render(request, 'index.html', context=d)


def blog_view(request):
    data = request.GET
    cat = data.get('cat', None)
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
        d = {
            'posts': posts,
            'blog': 'active'
        }
        return render(request, 'blog.html', context=d)

    posts = Post.objects.filter(is_published=True)
    post_obj = Paginator(posts, 2)

    d = {
        'posts': post_obj.get_page(page),
        'blog': 'active'
    }
    return render(request, 'blog.html', context=d)


def about_view(request):
    return render(request, 'about.html', context={'about': 'active'})


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(full_name=data['name'], email=data['email'], subject=data['subject'],
                                     message=data['message'])
        obj.save()
        text = f"""Project: MOOS 😎\nID: {obj.id}\nName: {obj.full_name}\nEmail: {obj.email}\nSubject is : {obj.subject}\nMessage: {obj.message}"""
        url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}'
        response = requests.get(url)
        return redirect('/contact')
    return render(request, 'contact.html', context={'contact': 'active'})


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(name=data['name'], email=data['email'], message=data['message'], post_id=pk)
        obj.save()
        post = Post.objects.get(id=pk)
        post.comments_count += 1
        post.save(update_fields=['comments_count'])

        return redirect(f'/blog/{pk}')

    post = Post.objects.get(id=pk)
    post.views_count += 1
    post.save(update_fields=['views_count'])
    comments = Comment.objects.filter(post_id=pk, is_published=True)
    d = {'post': post, 'comments': comments, 'comments_count': len(comments)}
    return render(request, 'blog-single.html', context=d)
