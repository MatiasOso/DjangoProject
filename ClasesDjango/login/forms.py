from django import forms


# La receta necesita: Categoria,Nombre,Ingredientes,Preparacion, Calificacion(1 al 5), Autor (ID)
class CreateNewRecipe(forms.Form):
    categoria = forms.CharField(label='Categoria', max_length=255, widget=forms.TextInput(attrs={'class': 'input mb-3'}))
    nombre = forms.CharField(label='Nombre', max_length=255, widget=forms.TextInput(attrs={'class': 'input'}))
    ingredientes = forms.CharField(label='Ingredientes', widget=forms.Textarea(attrs={'class': 'input addIngredientes', 'rows': 5}))  # Cambio a Textarea
    preparacion = forms.CharField(label='Preparacion', widget=forms.Textarea(attrs={'class': 'input addPreparacion', 'rows': 10}))  # Cambio a Textarea
    calificacion = forms.IntegerField(label='Calificacion', initial=0, widget=forms.TextInput(attrs={'class': 'input', 'readonly': True}))  # Establece 'initial' a 0 y 'readonly' a True
    autor = forms.IntegerField(label='Autor', initial=1, widget=forms.TextInput(attrs={'class': 'input', 'readonly': True})) 
    
class AddImage(forms.Form):
    img = forms.ImageField
    

#  INSERT into Comentario (Usuario,Receta_ID,Comentario) VALUES (3,'5','Hola este es un comentario de prueba :p') 
class Comentario(forms.Form):
    Usuario = forms.IntegerField(label='Usuario', widget=forms.TextInput(attrs={'class': 'input'}))
    Receta_ID = forms.IntegerField(label='Receta_ID', widget=forms.TextInput(attrs={'class': 'input'}))
    Comentario = forms.CharField(label='Comentario', max_length=255, widget=forms.TextInput(attrs={'class': 'input'}))
    
    