from django import forms


class InputForms(forms.Form):
    origin = forms.CharField(label='Origin', widget=forms.Textarea(attrs={"rows":5}))
    