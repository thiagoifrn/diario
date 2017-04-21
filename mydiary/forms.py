from django import forms

from .models import Diario

class DiarioForm(forms.ModelForm):

    class Meta:
        model = Diario
        fields = ('tarefa', )

class  FormEdit(forms.ModelForm):

    class Meta:
         model = Diario
         fields = ('resultados', 'avaliacao', 'atividades_futuras',)
