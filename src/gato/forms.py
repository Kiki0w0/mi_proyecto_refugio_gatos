from django import forms

from gato.models import Categoria, Gato, SolicitudAdopcion


class CategoriaForm(forms.ModelForm):  
    class Meta:
        model = Categoria
        # fields = ["nombre", "descripcion"]
        fields = "__all__"

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get("nombre", "")

        # Validar longitud
        if len(nombre) < 3:
            raise forms.ValidationError("Debe tener al menos 3 caracteres.")

        # Validar que sean solo letras o espacios
        for caracter in nombre:
            if caracter.isalpha() or caracter.isspace():
                continue
            else:
                raise forms.ValidationError("Solo se permiten letras y espacios.")
        return nombre


class GatoForm(forms.ModelForm):
    class Meta:
        model = Gato
        fields = "__all__"



class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = "__all__"
