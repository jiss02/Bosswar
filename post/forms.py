from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['mission_number','title','content','urlcontent','description']
        #writer, mission_number 삭제예정

        widgets = {
            'title':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': '제목을 입력하세요',
                }
            ),
            'content':forms.FileInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'urlcontent':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': '유튜브 링크를 입력하세요',
                }
            ),
            'description':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'rows': '5',
                    'placeholder': '내용을 입력하세요',
                }
            )
        }