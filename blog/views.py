from blog.models import BlogEntry, Category

from django.shortcuts import get_object_or_404, render_to_response


def index(request):
    entries = BlogEntry.objects.published()
    return render_to_response('blog/index.html', {'entries': entries}, request.FILES)

def category(request, id, slug):
    category = get_object_or_404(Category, id=id,
                                           slug=slug)
    entries = category.entries.published()
    return render_to_response('blog/index.html', {'entries': entries})

def archive_year(request, year):
    entries = BlogEntry.objects.filter(draft=False,
                                       published_at__year=year)
    return render_to_response('blog/index.html', {'entries': entries})

def archive_month(request, year, month):
    entries = BlogEntry.objects.filter(draft=False,
                                       published_at__year=year,
                                       published_at__month=month)
    return render_to_response('blog/index.html', {'entries': entries})

def archive_day(request, year, month, day):
    entries = BlogEntry.objects.filter(draft=False,
                                       published_at__year=year,
                                       published_at__month=month,
                                       published_at__day=day)
    return render_to_response('blog/index.html', {'entries': entries})

def details(request, year, month, day, slug):
    entry = get_object_or_404(BlogEntry, draft=False,
                                         published_at__year=year,
                                         published_at__month=month,
                                         published_at__day=day,
                                         slug=slug)
    return render_to_response('blog/details.html', {'entry': entry})
