import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product
import qrcode
from qrcode import *
from django.contrib.auth.decorators import user_passes_test, login_required
from newspaper_project.decorators import is_admin, is_adminwilaya, is_client, is_livreur
import json
from django.core.mail import send_mail
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()

file = open('/home/ubuntu/Bureau/news/products/wilayas.json')
data = json.load(file)



"""def get_communes(request):
    wilaya = request.POST.get('user_wilaya')
    COMMUNE_CHOICES = {}
    for el in data :
        if el == wilaya :
            for com in wilaya:
                COMMUNE_CHOICES.[append(com)]
    COMMUNE_CHOICES = COMMUNE_CHOICES.values('Commune_Name')
    response_data = {
        "communes" : COMMUNE_CHOICES
    }
    return JsonResponse(response_data)"""

@login_required
@user_passes_test(is_client)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        user = request.user
        email = user.email
        product = form.save(commit=False)
        product.email = email
        product.pretaexpedier = True
        product.save()
        form = ProductForm()
        return redirect('pret_a_expedier')
    context = {
        'form': form
    }
    return render(request, "products/new_product_create.html", context)


def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        product = form.save(commit=False)
        product.pretaexpedier = True
        product.save()
        return redirect('pret_a_expedier')
    context = {
        'form': form
    }
    return render(request, "products/new_product_create.html", context)

@login_required
@user_passes_test(is_client)

def product_list_view_client(request):
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

@login_required
@user_passes_test(is_adminwilaya)

def product_list_view_adminwilaya(request):
    user = request.user
    wilaya = user.wilaya
    queryset = Product.objects.filter(wilaya = wilaya) # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

@login_required

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("static/image/test.png")
    return render(request, "products/product_detail.html", context)

@login_required

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        users = User.objects.filter(groups__name = 'Livreurs')
        for user in users :
            colis = user.en_cours_livraison
            a = colis.split(';')
            colis = ''
            for element in a:
                if element != str(id):
                    colis += ';' + element
            idd = user.id
            user.objects.update(id = idd)
        obj.delete()
        return redirect('pret_a_expedier')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

@login_required
@user_passes_test(is_livreur)

def colis_payé(request, id):
    obj = Product.objects.filter(id = id)
    if request.method == "POST":
        prix = request.POST.get("price")
        obj.update(payés = prix)
        obj.update(enlivraison = False)
        user = request.user
        en_cours_livraison = user.en_cours_livraison
        a = en_cours_livraison.split(';')
        colis = ""
        livres = user.livres
        for item in a:
            if item != '' and item != id:
                colis += ';' + item
        livres = livres + ';' + str(id)
        idd = user.id
        print(colis)
        print(livres)
        CustomUser.objects.filter(id = idd).update(en_cours_livraison = colis)
        CustomUser.objects.filter(id = idd).update(livres = livres)
        idd = user.id
        CustomUser.objects.filter(id = idd).update(en_cours_livraison = '')
        CustomUser.objects.filter(id = idd).update(livres = livres)
        obj = Product.objects.get(id = id)
        email = obj.email
        body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + str(obj.id) + " à destination vers " + obj.email + ' et envoyé à '+ obj.nometpren + " est bien arrivé.\nWorld Express vous remercie pour votre confiance."
        send_mail(
            'World Express notifications - Colis arrivé à destination',
            body_text,
            'from@example.com',
            [email],
            fail_silently=False,
        )
    return redirect("en_livraison_livreur")

@login_required
@user_passes_test(is_livreur)

def colis_non_payé(request,id):
    obj = Product.objects.filter(id = id)
    if request.method == "POST":
        obj.update(enlivraison = False)
        user = request.user
        en_cours_livraison = user.en_cours_livraison
        a = en_cours_livraison.split(';')
        colis = ""
        livres = user.livres
        for item in a:
            if item != '' and item != id:
                colis += ';' + item
        livres = livres + ';' + str(id)
        idd = user.id
        print(colis)
        print(livres)
        CustomUser.objects.filter(id = idd).update(en_cours_livraison = colis)
        CustomUser.objects.filter(id = idd).update(livres = livres)
        obj = Product.objects.get(id = id)
        body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + str(obj.id) + " à destination vers " + obj.email + ' et envoyé à '+ obj.nometpren + " est bien arrivé, merci de nous payer dans les plus brefs délais.\nWorld Express vous remercie pour votre confiance."
        send_mail(
            'World Express notifications - Colis arrivé à destination',
            body_text,
            'from@example.com',
            [obj.email],
            fail_silently=False,
        )
    return redirect("en_livraison_livreur")

@login_required
@user_passes_test(is_livreur)

def non_payés(request,id):
    obj = Product.objects.filter(id = id)
    if request.method == "POST":
        prix = request.POST.get("price")
        obj.update(payés = prix)
        
    return redirect("livreur_non_payés")

@login_required
@user_passes_test(is_livreur)

def retour_chez_livreur(request,id):
    obj = Product.objects.filter(id = id)
    if request.method == "POST":
        obj.update(enlivraison = False)
        obj.update(retour_chez_livreur = True)
        for query in obj:
            email = query.email
        body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + obj.id + " à destination vers " + obj.wilaya + ' et envoyé à '+ obj.nometpren + " a subi un retour avec le livreur.\nWorld Express vous remercie pour votre confiance."
        send_mail(
                'World Express notifications - Colis suspendu',
                body_text,
                'from@example.com',
                [email],
                fail_silently=False,
        )
    return redirect("en_livraison_livreur")

@login_required

def retour_suspendre(request,id):
    obj = Product.objects.filter(id = id)
    if request.method == "POST":
        obj.update(suspendus = True)
        obj.update(retour_chez_livreur = False)
    return redirect("administrateur")

def all_suspendre(request,id):
    obj = Product.objects.get(id = id)
    if request.method == "POST":
        print('here')
        idd = obj.id
        Product.objects.filter(id=int(idd)).update(suspendus=False)
        query = Product.objects.get(id=int(idd))
        email = query.email
        body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + str(query.id) + " à destination vers " + query.wilaya + ' et envoyé à '+ query.nometpren + " a été suspendu, soit à votre demande, soit à cause d'un problème interne.\nWorld Express vous remercie pour votre confiance et s'excuse pour les désagréments."
        send_mail(
            'World Express notifications - suspension',
            body_text,
            'from@example.com',
            [email],
            fail_silently=False,
        )
    return redirect("administrateur")

@login_required

def retour_hub(request,id):
    obj = Product.objects.filter(id = id)
    if request.method == "POST":
        obj.update(enhub = True)
        obj.update(retour_chez_livreur = False)
    return redirect("administrateur")



@login_required
@user_passes_test(is_client)

def valider_colis_pret_a_expedier(request, id=id):
    Product.objects.filter(id=id).update(entransit=True)
    Product.objects.filter(id=id).update(pretaexpedier=False)
    return redirect('/client/pret_a_expedier') 

@login_required

def product_list_view(request):
    queryset = Product.objects.filter() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)