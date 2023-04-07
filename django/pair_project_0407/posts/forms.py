from .models import Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        )
    )

    CHOICES = [
        ('개발', '개발'),
        ('CS', 'CS'),
        ('신기술', '신기술'),
    ]
    category = forms.ChoiceField(
        label='카테고리',
        widget=forms.Select(
            attrs={
                    'class': 'form-control',
                },
        ),
        choices=CHOICES
    )
    content = forms.CharField(
        label='내용',
        widget=CKEditorUploadingWidget(
            attrs={
                'class': 'form-control',
            },
        )
    )

    class Meta:
        model = Post
        fields = '__all__'