from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last Name"})
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    student_id = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Student ID"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Student ID"})
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Student ID"})
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "student_id",
            "password",
            "password_2",
        ]
