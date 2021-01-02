from django import forms


class InputForms(forms.Form):
    input_txt = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows":5,
                "placeholder": 'Please, input your text here.\nThen click in the buttons below :D',
                "autofocus": True
                }
            ), required=False, label='', )
