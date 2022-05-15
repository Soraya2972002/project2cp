from django import forms
from .models import Product
from dynamic_forms import DynamicField, DynamicFormMixin

class ProductForm(DynamicFormMixin, forms.ModelForm): 
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
                "pretaexpedier",
                'enramassage',
                "entransit",
                'enhub',
                "enlivraison",
                'suspendus',
                "payés",
                "retour_chez_livreur",
                "email",
                'date',
                'checked'
        ]
        widgets = {
            'adresse': forms.TextInput(attrs={'placeholder': 'entrez votre adresse'}),
            'remarque': forms.Textarea(
                attrs={"placeholder": "ecrivez vos remarque a propos de l'envoi ici",}),
            'produit': forms.Textarea(
                attrs={'placeholder': 'décrivez le produit ici'}),
            #'wilaya' : forms.TextInput(attrs={'id': 'wilaya_id'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['date'].required = False
        self.fields['remarque'].required = False


