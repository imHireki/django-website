from django import forms


class InputForms(forms.Form):
    input_txt = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows":5,
                "autofocus": True
                }
            ), required=False, label='')
