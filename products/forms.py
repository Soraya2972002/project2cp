from tkinter import Widget
from django import forms
from .models import Product,Feedback

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
                'checked',
        ]
        widgets = {
            'adresse': forms.TextInput(attrs={'placeholder': ' entrez votre adresse'}),
            'nometpren': forms.TextInput(attrs={'placeholder': ' entrez votre nom et prénom'}),
            'remarque': forms.TextInput(
                attrs={"placeholder": " ecrivez vos remarque a propos de l'envoi ici",}),
            'produit': forms.TextInput(
                attrs={'placeholder': ' décrivez le produit ici'}),
            'poids': forms.TextInput(
                attrs={'placeholder': ' entrez le poids'}),
            'numerocommande': forms.TextInput(
                attrs={'placeholder': ' entrez le numéro de commande'}),
            'montant': forms.TextInput(
                attrs={'placeholder': ' entrez le montant'}),
            'telephone': forms.TextInput(
                attrs={'placeholder': ' entrez le numéro de telephone'}),
            'telephone1': forms.TextInput(
                attrs={'placeholder': ' entrez le numéro de telephone (optionel) '}),
            'commune': forms.TextInput(
                attrs={'placeholder': ' entrez la commune '}),
            #'wilaya' : forms.TextInput(attrs={'id': 'wilaya_id'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['date'].required = False
        self.fields['remarque'].required = False
        self.fields['produit'].required = False
        self.fields['telephone1'].required = False
        self.fields['numerocommande'].required = False
        self.fields['payés'].required = False

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'comment'
        ]
    widgets = {
        'comment' : forms.Textarea(
            attrs={
                "class" : 'field',
                'placeholder': 'décrivez le produit ici'
            }
        )
    }

