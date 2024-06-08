from django import forms

class SubirExcel(forms.Form):
    archivo = forms.FileField(label="Selecciona un archivo Excel")