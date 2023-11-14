from django import forms

# La receta necesita: Categoria,Nombre,Ingredientes,Preparacion, Calificacion(1 al 5), Autor (ID)
class CreateNewRecipe(forms.Form):
    categoria = forms.CharField(label='Categoria', max_length=255, widget=forms.TextInput(attrs={'class': 'input'}))
    nombre = forms.CharField(label='Nombre', max_length=255, widget=forms.TextInput(attrs={'class': 'input'}))
    ingredientes = forms.CharField(label='Ingredientes', max_length=255, widget=forms.TextInput(attrs={'class': 'input addIngredientes'}))
    preparacion = forms.CharField(label='Preparacion', max_length=300, widget=forms.TextInput(attrs={'class': 'input addPreparacion'}))
    calificacion = forms.IntegerField(label='Calificacion', widget=forms.TextInput(attrs={'class': 'input'}))
    autor = forms.IntegerField(label='Autor', widget=forms.TextInput(attrs={'class': 'input'}))
