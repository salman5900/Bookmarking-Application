from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark,File
from urllib.parse import urlparse
from django.contrib.auth.decorators import login_required
from . import forms
from collections import defaultdict
# Create your views here.


@login_required
def dashboard(request):
    user = request.user
    bookmarks = Bookmark.objects.filter(user=user).select_related('folder').order_by('-created_at')

    others = []
    grouped_bookmarks = defaultdict(list)
    for bookmark in bookmarks:
        if bookmark.folder:
            grouped_bookmarks[bookmark.folder.name].append(bookmark)
        else:
            others.append(bookmark)

    folder_names = File.objects.filter(name__in=grouped_bookmarks.keys(), user=user)

    # Add favicon
    for bm in bookmarks:
        domain = urlparse(bm.url).netloc
        bm.favicon_url = f"https://www.google.com/s2/favicons?sz=64&domain={domain}"

    return render(request, 'Dashboard/dashboard.html', {
        'bookmarks': bookmarks,
        'grouped_bookmarks': dict(grouped_bookmarks),
        'folder_names': folder_names,
        'others': others,
        'user': user,
    })


def acces_each_file(request, slug):
    Folder = Folder.objects.get(slug=slug, user=request.user)

    bookmarks = Bookmark.objects.filter(user=request.user, folder=Folder).order_by('-created_at')

    return render(request, 'Dashboard/acces_each_file.html', {
        'bookmarks': bookmarks,
        'file': Folder,
    })

@login_required
def edit_bookmark(request, slug):
    bookmark = Bookmark.objects.get(slug=slug)
    if request.method == "POST":
        form = forms.BookmarkForm(request.POST, request.FILES, instance=bookmark)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user  
            bookmark.save() # auto generate slug
            return redirect('Dashboard:dashboard')
    else:
        form = forms.BookmarkForm(instance=bookmark)
    return render(request, 'Dashboard/edit_bookmark.html', {'form': form, 'bookmark': bookmark})

@login_required
def add_bookmark(request):
    if request.method == "POST":
        form = forms.BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user  
            bookmark.save() # auto generate slug
            return redirect('Dashboard:dashboard')
    else:
        form = forms.BookmarkForm()
    
    return render(request, 'Dashboard/add_bookmark.html', {'form': form})

@login_required
def delete_bookmark(request, slug):
    bookmark = Bookmark.objects.get(slug=slug, user=request.user)
    bookmark.delete()
    return redirect('Dashboard:dashboard')

@login_required
def files(request):
    if request.method == "POST":
        form = forms.FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user  
            file.save()
            return redirect('Dashboard:dashboard')
    else:
        form = forms.FileForm()
    return render(request, 'Dashboard/files.html', {'form': form})