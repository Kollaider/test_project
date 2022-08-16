from django.http import HttpRequest
from django.shortcuts import render
from blog.models import Entry, Blog, Author

def home(request):
    entries = Entry.objects.all()
    context = {'entries': entries}
    return render(request, 'blog/index.html', context=context)
