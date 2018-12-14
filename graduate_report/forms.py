from django import forms


class ImportExelForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'}))
