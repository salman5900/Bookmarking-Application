from django.shortcuts import render, redirect
from .models import Bookmark
from urllib.parse import urlparse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def dashboard(request):
    bookmarks = bookmarks = Bookmark.objects.filter(user=request.user).order_by('-created_at')

    # Extract logo each url 
    for bm in bookmarks:
        domain = urlparse(bm.url).netloc
        bm.favicon_url = f"https://www.google.com/s2/favicons?sz=64&domain={domain}"
    return render(request, 'Dashboard/dashboard.html', {'bookmarks': bookmarks})

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
