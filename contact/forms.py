from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(attrs={"placeholder": "Tu nombre"}),
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"placeholder": "tu@email.com"})
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={"placeholder": "Escribe tu mensaje aquí...", "rows": 5}
        ),
    )
