from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist', 'released', 'bio', 'album_art')


# class FavoriteForm(forms.ModelForm):
#     class Meta:
#         model = Favorite
#         fields = ['user', 'album', 'is_favorite']
