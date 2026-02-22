from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your name"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Enter your message",
            "rows": 4
        })
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name should contain only letters.")
        return name

    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get("message")

        if message and "django" not in message.lower():
            raise forms.ValidationError(
                "Message must mention 'Django' to ensure relevance."
            )

        return cleaned_data
