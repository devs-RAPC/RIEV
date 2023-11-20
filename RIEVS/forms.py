from django import forms
from django.core.exceptions import ValidationError
from .models import Topic
from .models import Publication


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']
        labels = {'title': ''}


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'text', 'image']
        labels = {'title': '', 'text': '', 'image': ''}
        name = {'image': 'my_img'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # Verifica o tamanho máximo da imagem (em bytes)
            max_size = 5 * 1024 * 1024  # 2 MB como exemplo, ajuste conforme necessário

            if image.size > max_size:
                raise ValidationError('A imagem não pode ser maior que 5 MB.')

        return image
