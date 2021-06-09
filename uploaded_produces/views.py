from django.shortcuts import render
from uploaded_produces.models import FillProduceDetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def abstract_view(request):
    projects = FillProduceDetails.objects.all()
    paginator = Paginator(projects, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    context = {
        'projects': posts
    }

    return render(request, 'abstract_view.html', context)


def detail_view(request, pk):
    project = FillProduceDetails.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'detail_view.html', context)

