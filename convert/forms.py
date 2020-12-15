from django import forms


class InputForms(forms.Form):
    input_txt = forms.CharField(widget=forms.Textarea(attrs={"rows":5}), required=False, label='')
    