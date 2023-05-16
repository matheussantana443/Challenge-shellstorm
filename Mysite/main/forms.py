from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    data_envio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora_envio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    tipo_email = forms.CharField(max_length=100)
    setor = forms.CharField(max_length=100)
