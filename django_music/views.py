from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Album, Favorite
from .forms import AlbumForm
from django_music.models import User
from django.http import JsonResponse


def homepage(request):
    return render(request, 'index.html')


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})


def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    # Get other albums by the same artist, excluding the current album
    other_albums = Album.objects.filter(
        artist=album.artist).exclude(pk=album.pk)

    context = {
        'album': album,
        'other_albums': other_albums,
    }

    return render(request, 'album_detail.html', context)


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)

    return render(request, 'album_form.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'album_confirm_delete.html', {'album': album})


def toggle_favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    user = request.user

    # If the album is already in the user's favorites, toggle it
    if album in user.favorites.all():
        # user.favorites represents a related manager for the Favorite model
        # allows you to access the Favorite objects related to a specific user
        favorite = user.favorites.get(album=album)
        # toggle favorite on/off
        favorite.is_favorite = not favorite.is_favorite
        favorite.save()
    else:
        favorite = Favorite(user=user, album=album, is_favorite=True)
        favorite.save()

    return redirect('album_detail', pk=album_id)
