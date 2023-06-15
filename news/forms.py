from django.forms import ModelForm, TextInput, Textarea, Select, SelectMultiple

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["author", "category", "title", "text"]
        widgets = {
            "author": Select(
                attrs={
                    "class": "custom-select",
                }
            ),
            "category": SelectMultiple(
                attrs={
                    "multiple class": "form-control",
                }
            ),
            "text": Textarea(
                attrs={"class": "form-control", "placeholder": "Введите текст"}
            ),
        }
