from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name1",
            "last_name2",
            "birth_date",
            "baptism_date",
            "estado",
            "phone",
            "address",
            "reparto",
            "municipality",
            "photo",
            "notes",
        ]
        widgets = {
            "birth_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;",
                }
            ),
            "baptism_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                }
            ),
            "reparto": forms.TextInput(
                attrs={
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                }
            ),
            "municipality": forms.TextInput(
                attrs={
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"
                }
            ),
            "photo": forms.FileInput(attrs={"style": "width: 100%; padding: 8px;"}),
            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                    "style": "width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;",
                }
            ),
        }
