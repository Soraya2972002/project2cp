from django import forms
from .models import Product

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ["nometpren", 
                "telephone", 
                "telephone1",
                'wilaya',
                "commune",
                "adresse",
                "montant",
                "numerocommande",
                "poids",
                'remarque',
                'produit',
                'typeenvoi',
                'typeprestation',
        ]
        widgets = {
            'adresse': forms.TextInput(attrs={'placeholder': 'entrez votre adresse'}),
            'remarque': forms.Textarea(
                attrs={'placeholder': 'ecrivez vos remarque a propos de lenvoi ici',
                "rows" : 20,
                "cols" : 50}),
            'produit': forms.Textarea(
                attrs={'placeholder': 'décrivez le produit ici'}),
        }
    def clean_number(self, *args, **kwargs):
        x = ['telephone','telephone1']
        for i in x:
            number = str(self.cleaned_data.get(i))
            if number[:2] != '05' or  number[:2] != '07' or number[:2] != '06':
                raise forms.ValidationError('This is not a valid phone number')
        return number
    def clean_nompren(self, *args, **kwargs):
        n = self.cleaned_data.get("nometpren")
        if ' ' not in n:
            raise forms.ValidationError('This is not valid')
        return n