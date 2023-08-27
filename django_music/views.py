from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Album
from .forms import AlbumForm
from django_music.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# @login_required
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

    prev_album = Album.objects.filter(pk__lt=album_id).order_by('-pk').first()
    next_album = Album.objects.filter(pk__gt=album_id).order_by('pk').first()

    has_prev_album = prev_album is not None
    has_next_album = next_album is not None

    # Get other albums by the same artist, excluding the current album
    other_albums = Album.objects.filter(
        artist=album.artist).exclude(pk=album.pk)

    context = {
        'album': album,
        'prev_album': prev_album,
        'next_album': next_album,
        'other_albums': other_albums,
        'has_prev_album': has_prev_album,
        'has_next_album': has_next_album,
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


@csrf_exempt
def toggle_favorite(request, album_id):
    if request.method == "POST":
        album = get_object_or_404(Album, pk=album_id)
        # user = request.user()  <= after authentication
        user = User.objects.get(pk=1)  # <= force user until auth is working
        print(user.favorites.all())

        if album in user.favorites.all():
            user.favorites.remove(album)
            is_favorite = False
        else:
            user.favorites.add(album)
            is_favorite = True

        return JsonResponse({"is_favorite": is_favorite})

    return JsonResponse({}, status=400)
