from django import forms
from .models import Album, Favorite


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['album_art'].widget.attrs.update({'accept': 'image/*'})


# class FavoriteForm(forms.ModelForm):
#     class Meta:
#         model = Favorite
#         fields = ['user', 'album', 'is_favorite']
