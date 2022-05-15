from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
import datetime
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from products.models import Product
from django.contrib.auth.decorators import user_passes_test, login_required
from newspaper_project.decorators import is_admin, is_adminwilaya, is_client, is_livreur
from django.core.mail import send_mail
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
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
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
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
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
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
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

def pret_a_expedier_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = Product.objects.filter(pretaexpedier = True)
    queryset = queryset.filter(suspendus = False)
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


def hub_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
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

@login_required
@user_passes_test(is_admin)

def afficher_livreurs(request):
    users = User.objects.filter(groups__name = 'Livreurs')
    context = {
        "users": users
    }
    return render(request, 'list_livreur.html', context)

@login_required
@user_passes_test(is_admin)

def afficher_clients(request):
    users = User.objects.filter(groups__name = None)
    context = {
        "users": users
    }
    return render(request, 'list_livreur.html', context)

@login_required
@user_passes_test(is_admin)

def selectionner_transit(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('selection')
        choice =  request.POST.get('Choices')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(checked=True)
                if choice == '0': #delete
                    if idd != '':
                        Product.objects.filter(id=int(idd)).delete()
                if choice == "1": #choose delivery
                    return redirect('choisir_livreurs')    
                if choice == '2': # validate
                    if idd != '':
                        Product.objects.filter(id=int(idd)).update(checked=False)
                        Product.objects.filter(id=int(idd)).update(entransit=False)
                        Product.objects.filter(id=int(idd)).update(enhub=True)
                if choice == '3': # suspendre
                    if idd != '':
                        Product.objects.filter(id=int(idd)).update(suspendus=True)
                        Product.objects.filter(id=int(idd)).update(enlivraison=False)
                        query = Product.objects.get(id=int(idd))
                        email = query.email
                        body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + query.id + " à destination vers " + query.wilaya + ' et envoyé à '+ query.nometpren + " a été suspendu, soit à votre demande, soit à cause d'un problème interne. Vous serez tenu au courant.\nWorld Express vous remercie pour votre confiance."
                        send_mail(
                            'World Express notifications - Colis suspendu',
                            body_text,
                            'from@example.com',
                            [email],
                            fail_silently=False,
                        )

    return redirect('expedier_admin')

@login_required
@user_passes_test(is_admin)

def selectionner_suspendus(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(suspendus=False)
                query = Product.objects.get(id=int(idd))
                email = query.email
                body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + query.id + " à destination vers " + query.wilaya + ' et envoyé à '+ query.nometpren + " n'est plus suspendu.\nWorld Express vous remercie pour votre confiance."
                send_mail(
                    'World Express notifications - arrêt de suspension',
                    body_text,
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )

@login_required
@user_passes_test(is_livreur)

def selectionner_livreur_ramassage(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(enramassage=False)
                Product.objects.filter(id=int(idd)).update(enlivraison=True)
            
@login_required
@user_passes_test(is_livreur)

def selectionner_livreur_livraison(request):
    if request.method == 'POST':
        user = request.user
        en_cours_livraison = user.en_cours_livraison
        livres = user.livres
        livres = livres + en_cours_livraison
        idd = user.id
        CustomUser.objects.get(id = idd).update(en_cours_livraison = '')
        CustomUser.objects.get(id = idd).update(livres = livres)
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(enlivraison=False)
                query = Product.objects.get(id=int(idd))
                email = query.email
                body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + query.id + " à destination vers " + query.email + ' et envoyé à '+ query.nometpren + " est bien arrivé.\nWorld Express vous remercie pour votre confiance."
                send_mail(
                    'World Express notifications - Colis arrivé à destination',
                    body_text,
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )


@login_required
@user_passes_test(is_admin)

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
        idd = request.POST.get('submit', None)
        search_time = request.POST.get('time', None)
        queryset = Product.objects.filter(checked = True)
        s = ''
        compte = 0
        for product in queryset:
            product.update(enhub = False)
            product.update(enramassage = True)
            s += ";" + str(product.id)
            compte += 1
        CustomUser.objects.filter(id=int(idd)).update(en_cours_livraison = s)
        CustomUser.objects.filter(id=int(idd)).update(date = search_date + " " + search_time)
        Product.objects.filter(checked = True).update(checked = False)
        body_text = 'Bonjour,\nWorld Express vous informe que vous avez ' + str(compte) + " colis à venir récupérer avant le " + search_date + ' à '+ search_time + '.\nSalutations.'
        send_mail(
            'World Express notifications - Nouveaux Colis',
            body_text,
            'from@example.com',
            [CustomUser.objects.get(id=idd).email],
            fail_silently=False,
        )
        return redirect("expedier_admin")
    return render(request, 'choisir_livreurs.html', context)

@login_required
@user_passes_test(is_admin)

def transit_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = Product.objects.filter(entransit = True)
    queryset = queryset.filter(suspendus = False)
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
    return render(request,'en_transit_admin.html',context)


@login_required
@user_passes_test(is_livreur)

def a_recuperer_livreur_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email)
    queryset = queryset.filter(suspendus = False) 
    a = user.en_cours_livraison
    l = a.split(';')
    for el in a:
        queryset.union(queryset,Product.objects.get(id = int(el)))
    queryset = queryset.filter(entransit = True)
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
    return render(request,'a_recuperer_livreur.html',context)

@login_required
@user_passes_test(is_livreur)
    
def en_livraison_livreur_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    queryset = Product.objects.filter(username = '')
    a = user.en_cours_livraison
    l = a.split(';')
    for el in a:
        queryset.union(queryset,Product.objects.get(id = int(el)))
    queryset = queryset.filter(enlivraison = True)
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
    return render(request,'en_livraison_livreur.html',context)

@login_required
@user_passes_test(is_livreur)

def historique_livreur_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    livres = user.livres
    l = livres.split(';')
    Product.objects.all().order_by('date')
    queryset = Product.objects.filter(nometpren = '')
    for idd in l:
        if idd != '':
            queryset.union(queryset,Product.objects.get(id = int(idd)))
    queryset = queryset.filter(suspendus = False)
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
    return render(request,'historique_livreur.html',context)

@login_required
@user_passes_test(is_admin)

def historique_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    search_date1 = request.POST.get('first_date', None)
    search_date2 = request.POST.get('second_date', None)
    search_price1 = request.POST.get('first_number', None)
    search_price2 = request.POST.get('second_number', None)
    Product.objects.all().order_by('date')
    queryset = Product.objects.filter(pretaexpedier = False).filter(enramassage = False).filter(entransit = False).filter(enhub = False).filter(enlivraison = False).filter(suspendus = False)
    somme = 0
    for el in queryset:
        somme += int(el.payés)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
    if search_date1 != None and search_date2 != None :
        new_queryset = queryset
        for el in queryset:
            date = el.date
            l = date.split(' ')
            li = l[0].split('-')
            l1 = search_date.split("-")
            l2 = search_date.split('-') 
            date = datetime.date(l[0],l[1],l[2]) 
            date1 = datetime.date(l1[0],l1[1],l1[2]) 
            date2 = datetime.date(l2[0],l2[1],l2[2]) 
            if date >= date1 and date <= date2:
                new_queryset.union(new_queryset, el)
        queryset = new_queryset
    if search_price1 != None and search_price2 != 0:
        new_queryset = queryset
        for el in queryset :
            price = el.payés
            if price >= search_price1 and price <= search_price2:
                new_queryset.union(new_queryset, el)
        queryset = new_queryset

    queryset = queryset.order_by('date')
    context = {
        "object_list": queryset,
        'somme' : somme
    }
    return render(request,'historique_admin.html',context)

@login_required
@user_passes_test(is_client)

def historique_client_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    Product.objects.all().order_by('date')
    email = request.user.email
    queryset = Product.objects.filter(email = email)
    queryset = queryset.filter(pretaexpedier = False).filter(enramassage = False).filter(entransit = False).filter(enhub = False).filter(enlivraison = False).filter(suspendus = False)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
    queryset = queryset.order_by('date')
    context = {
        "object_list": queryset
    }
    return render(request,'historique_client.html',context)

@login_required
@user_passes_test(is_admin)

def en_hub_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(enhub = True) 
    queryset = queryset.filter(suspendus = False)
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
    return render(request,'en_hub_admin.html',context)

@login_required
@user_passes_test(is_admin)

def en_livraison_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(enlivraison = True) 
    queryset = queryset.filter(suspendus = False)
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
    return render(request,'en_livraison_admin.html',context)

@login_required
@user_passes_test(is_admin)

def en_ramassage_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(enramassage = True) 
    queryset = queryset.filter(suspendus = False)
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
    return render(request,'en_ramassage_admin.html',context)

@login_required
@user_passes_test(is_admin)

def suspendus_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(suspendus = True) 
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
    return render(request,'suspendus_admin.html',context)

@login_required
@user_passes_test(is_client)

def suspendus_client_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.filter(suspendus = True) 
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
    return render(request,'suspendus_client.html',context)

@login_required
@user_passes_test(is_livreur)

def livreur_non_payés(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    livres = user.livres
    l = livres.split(';')
    Product.objects.all().order_by('date')
    queryset = Product.objects.filter(nometpren = '')
    for idd in l:
        if idd != '':
            queryset.union(queryset,Product.objects.get(id = int(idd)))
    queryset = queryset.filter(payés = 0)
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
    return render(request,'livreur_non_payés.html',context)

@login_required
@user_passes_test(is_admin)

def retour_livreur_admin(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(retour_livreur = True) 
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
    return render(request,'retour_livreur_admin.html',context)

@login_required
@user_passes_test(is_client)

def payes_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.exclude(payés = 0)
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
    return render(request,'payes_client.html',context)

@login_required
@user_passes_test(is_client)

def non_payes_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.filter(payés = 0)
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
    return render(request,'non_payes_client.html',context)

@login_required
@user_passes_test(is_client)

def historique_payements_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.exclude(payés = 0)
    somme = 0
    for el in queryset:
        somme += int(el.payés)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
    context = {
        "object_list": queryset,
        'somme' : somme
    }
    return render(request,'historique_payements_client.html',context)

@login_required
@user_passes_test(is_client)

def retour_livreur_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.filter(retour_chez_livreur = True)
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
    return render(request,'retour_livreur_client.html',context)