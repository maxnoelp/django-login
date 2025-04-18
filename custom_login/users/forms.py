from django import forms

from .models import User, UserProfile


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "id": "floatingInput",
            },
        ),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_2",
        ]

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("password")
        pw2 = cleaned_data.get("password_2")
        if pw1 and pw2 and pw1 != pw2:
            self.add_error("password_2", "Passwörter stimmen nicht überein!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(
            commit=False
        )  # Erstmal das ModelForm speichern, aber nicht in DB
        user.set_password(self.cleaned_data["password"])  # Passwort-Hash
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control form-control-lg",
                "id": "floatingInput",
            },
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-lg",
                "id": "floatingInput",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class UserProfileForm(forms.ModelForm):
    cover_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Cover Image",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )
    profile_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "placeholder": "Cover Image",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )

    job_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Job Bezeichnung",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )

    biographie = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Biographie",
                "class": "form-control",
                "id": "floatingInput",
            }
        )
    )

    class Meta:
        model = UserProfile
        fields = [
            "profile_image",
            "cover_image",
            "biographie",
            "job_title",
        ]
