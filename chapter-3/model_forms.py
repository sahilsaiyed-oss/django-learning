from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """
    ModelForm for creating and updating BlogPost
    """

    class Meta:
        model = BlogPost
        fields = [
            "title",
            "content",
            "author",
            "is_published",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter blog title"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your content here..."
            }),
            "author": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Author name"
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if len(title) < 5:
            raise forms.ValidationError(
                "Title must be at least 5 characters long."
            )

        return title
