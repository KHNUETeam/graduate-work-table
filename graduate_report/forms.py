from django import forms


class ImportExelForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    }))


class SearchForm(forms.Form):
    phrases = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введіть словосполучення, слово або частину слова'
    }))
    start = forms.DateTimeField(required=False, widget=forms.DateInput(attrs={
        'class': 'form-control tcal',
        'placeholder': 'Дата початку',
        'name': 'date'
    }))
    end = forms.DateTimeField(required=False, widget=forms.DateInput(attrs={
        'class': 'form-control tcal',
        'placeholder': 'Дата закінчення',
        'name': 'date'

    }))
