from django.shortcuts import render
from upload_produces.models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def produce_index(request):
    projects = Post.objects.all().order_by('-created_on')
    paginator = Paginator(projects, 1)
    page = request.GET.get('page')
    try:
        posts_obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts_obj = paginator.page(paginator.num_pages)
    context = {
        "projects": posts_obj
    }
    return render(request, "produce_index.html", context)


def produce_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "produce_category.html", context)


def produce_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "produce_detail.html", context)
