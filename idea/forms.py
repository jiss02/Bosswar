from django import forms
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력하세요',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '7',
                    'placeholder': '내용을 입력하세요',
                }
            )
        }
        labels = {
            'title': '',
            'content': '',
        }