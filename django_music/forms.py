from django import forms
from .models import Album, Favorite


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist', 'album_art')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # First, define the 'album_art' field in the form
        self.fields['album_art'] = forms.ImageField(
            label='Album Art',
            required=False,
            widget=forms.FileInput(attrs={'accept': 'image/*'}),
        )

        # Then, update the widget attributes
        self.fields['album_art'].widget.attrs.update({'accept': 'image/*'})


# class FavoriteForm(forms.ModelForm):
#     class Meta:
#         model = Favorite
#         fields = ['user', 'album', 'is_favorite']
