from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime
import string
from accounts.models import CustomUser
from newspaper_project.decorators import is_admin, is_adminwilaya, is_client, is_livreur
from django.contrib.auth import get_user_model
from products.models import Product
from products.forms import ProductForm
User = get_user_model()

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,'index.html',{})
def contact_view(request, *args, **kwargs):
    my_context = {
        'my_text' : "This is about us",
        'This_is_true' : True,
        'my_number' : 123,
        'my_list' : [45,56,89]
    }
    print(request.user)
    return render(request,'contact.html',my_context)

@login_required
@user_passes_test(is_client)

def user_view(request, *args, **kwargs):
    return render(request,'main.html',{})

@login_required
@user_passes_test(is_admin)

def admin_view(request, *args, **kwargs):
    return render(request,'admin.html',{})

@login_required
@user_passes_test(is_adminwilaya)

def admin_wilaya_view(request, *args, **kwargs):
    return render(request,'admin_wilaya.html',{})

@login_required
@user_passes_test(is_livreur)

def livreur_view(request, *args, **kwargs):
    return render(request,'livreurs.html',{})

@login_required
@user_passes_test(is_client)

def ramassage_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    #search_etape = request.POST.get('etape', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(enramassage = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    context = {
        "object_list": queryset
    }
    return render(request,'En_ramassage.html',context)

@login_required
@user_passes_test(is_client)

def transit_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    #search_etape = request.POST.get('etape', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(entransit = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    context = {
        "object_list": queryset
    }
    return render(request,'En_transit.html',context)

@login_required
@user_passes_test(is_client)

def livraison_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    #search_etape = request.POST.get('etape', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(enlivraison = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    context = {
        "object_list": queryset
    }
    return render(request,'En-livraison.html',context)

@login_required
@user_passes_test(is_client)

def non_encaisse_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    #search_etape = request.POST.get('etape', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(nonencaissés = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    context = {
        "object_list": queryset
    }
    return render(request,'Non_encaisse.html',context)

@login_required
@user_passes_test(is_client)

def pret_a_expedier_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    #queryset = Product.objects.filter(email = email) 
    queryset = Product.objects.filter(pretaexpedier = True)
    print('date',search_date)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
    context = {
        "object_list": queryset
    }
    return render(request,'pret-a-expedier.html',context)


@login_required
@user_passes_test(is_client)

def suspendus_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    #search_etape = request.POST.get('etape', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    context = {
        "object_list": queryset
    }
    return render(request,'Suspendus.html',context)

@login_required
@user_passes_test(is_client)

def hub_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    #search_etape = request.POST.get('etape', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(enhub = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    context = {
        "object_list": queryset
    }
    return render(request,'En_hub.html',context)

def afficher_livreurs(request):
    users = User.objects.filter(groups__name = 'Livreurs')
    context = {
        "users": users
    }
    return render(request, 'list_livreur.html', context)
def afficher_clients(request):
    users = User.objects.filter(groups__name = None)
    context = {
        "users": users
    }
    return render(request, 'list_livreur.html', context)
def selectionner(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('selection')
        choice =  request.POST.get('Choices')
        for id in id_list:
            Product.objects.filter(id=id).update(checked=True)
            if choice == '0': #delete
                Product.objects.filter(id=id).delete()
            if choice == "1": #choose delivery
                return redirect('choisir_livreurs')    
            if choice == '2': # validate
                Product.objects.filter(id=id).update(checked=False) # will get changed later ; 

    return redirect('expedier_admin')
def choisir_livreur(request):
    users = User.objects.filter(groups__name = 'Livreurs')
    search_username = request.POST.get('username', None)
    if search_username != None:
        users = users.filter(username = search_username.lower())
    search_fname = request.POST.get('fname', None)
    if search_fname != None:
        users = users.filter(first_name = search_fname.lower())
    search_lname = request.POST.get('lname', None)
    if search_lname != None:
        users = users.filter(last_name = search_lname.lower())
    search_disponible = request.POST.get('etat', None)
    if search_disponible == '0':
        users = users.filter(disponible = True)
    if search_disponible == '1':
        users = users.filter(disponible = False)
    search_wilaya = request.POST.get('user_wilaya', None)
    if search_wilaya != '0' and search_wilaya!= None:
        users = users.filter(wilaya = search_wilaya)
    context = {
        "users": users
    }
    if request.POST.get('submit', None) != None:
        search_date = request.POST.get('date', None)
        print(search_date)
        idd = request.POST.get('submit', None)
        search_time = request.POST.get('time', None)
        print(search_time)
        queryset = Product.objects.filter(checked = True)
        s = ''
        for product in queryset:
            s += ";" + str(product.id)
        s = s[1:]
        CustomUser.objects.filter(id=idd).update(en_cours_livraison = s)
        CustomUser.objects.filter(id=idd).update(date = search_date + " " + search_time)
        Product.objects.filter(checked = True).update(checked = False)
        return redirect("expedier_admin")
    return render(request, 'choisir_livreurs.html', context)

def pret_a_expedier_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    #queryset = Product.objects.filter(email = email) 
    queryset = Product.objects.filter(pretaexpedier = True)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
    context = {
        "object_list": queryset
    }
    return render(request,'pret_a_expedier_admin.html',context)