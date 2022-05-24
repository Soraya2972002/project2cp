from xmlrpc.client import DateTime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils import timezone
import datetime
from django.contrib import messages
import pytz
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from products.models import Product,Feedback
from products.forms import FeedbackForm
from django.contrib.auth.decorators import user_passes_test, login_required
from newspaper_project.decorators import is_admin, is_adminwilaya, is_client, is_livreur
from django.core.mail import send_mail
User = get_user_model()
from django.contrib.auth.models import Group

# Create your views here.
def home_view(request, *args, **kwargs):
    user = ''
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Livreurs').exists():
            user = "livreur"
        elif request.user.is_superuser:
            user = "administrateur"
        else:
            user = "client"
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.id_user = -1
        obj.save()    
    context = {
        "form": form,
        "userr":user
    }

    return render(request,'index.html',context)
def contact_view(request, *args, **kwargs):
    my_context = {
        'my_text' : "This is about us",
        'This_is_true' : True,
        'my_number' : 123,
        'my_list' : [45,56,89]
    }
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
    l = []
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
    queryset = queryset.filter(enramassage = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
        l.append(search_wilaya)
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
        l.append(search_prestation)
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        l.append(search_type)
    context = {
        "object_list": queryset,
        'list' : l
    }
    return render(request,'En_ramassage.html',context)

@login_required
@user_passes_test(is_client)

def transit_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    l = []
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
    queryset = queryset.filter(entransit = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
        l.append(search_wilaya)
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation)
        l.append(search_prestation) 
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        l.append(search_type)
    context = {
        "object_list": queryset,
        'list' : l
    }
    return render(request,'En_transit.html',context)

@login_required
@user_passes_test(is_client)

def livraison_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    user = request.user
    l = []
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
    queryset = queryset.filter(enlivraison = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
        l.append(search_wilaya)
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
        l.append(search_prestation)
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        l.append(search_type)
    context = {
        "object_list": queryset,
        'list' : l
    }
    return render(request,'En-livraison.html',context)


@login_required
@user_passes_test(is_client)

def pret_a_expedier_view(request, *args, **kwargs):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    li = []
    email = user.email
    queryset = Product.objects.filter(email = email) 
    queryset = Product.objects.filter(pretaexpedier = True)
    queryset = queryset.filter(suspendus = False)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
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
    l = []
    queryset = Product.objects.filter(email = email) 
    queryset = queryset.filter(suspendus = False)
    queryset = queryset.filter(enhub = True)
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya) 
        l.append(search_wilaya)
    if search_prestation != "0" and search_prestation != None:
        queryset = queryset.filter(typeprestation = search_prestation) 
        l.append(search_prestation)
    if search_type != "0" and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        l.append(search_type)
    context = {
        "object_list": queryset,
        'list' : l
    }
    return render(request,'En_hub.html',context)

@login_required
@user_passes_test(is_admin)

def afficher_livreurs(request):
    users = User.objects.filter(groups__name = 'Livreurs')
    search_username = request.POST.get('username', None)
    li = []
    if search_username != None:
        users = users.filter(username = search_username.lower())
        li.append(search_username)
    search_fname = request.POST.get('fname', None)
    if search_fname != None:
        users = users.filter(first_name__iexact = search_fname.lower())
        li.append(search_fname)
    search_lname = request.POST.get('lname', None)
    if search_lname != None:
        users = users.filter(last_name__iexact = search_lname.lower())
        li.append(search_lname)
    somme = 0
    if request.POST.get('submit', None) != None:
        idd = request.POST.get('submit', None)
        users = User.objects.filter(id=idd)
        for user in users:
            email = user.email
            user.delete()
        body_text = "Bonjour,\nWorld Express vous informe que vous venez d'être licensié. Nous nous excusons et vous souhaitons plus de réussites personnelles"
        send_mail(
            'World Express notifications - Licenciement',
            body_text,
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return redirect('administrateur')
    if request.POST.get('submit1', None) != None:
        idd = request.POST.get('submit1', None)
        users = User.objects.filter(id=idd)
        for user in users:
            email = user.email
            user.delete()
        return redirect('administrateur')
    for user in users :
        somme += 1
    context = {
        "users": users,
        'userr' : 'livreurs',
        'somme' : somme,
        'list' : li
    }
    return render(request, 'list_livreur.html', context)

@login_required
@user_passes_test(is_admin)

def afficher_clients(request):
    users = User.objects.filter(groups__name = None)
    search_username = request.POST.get('username', None)
    li = []
    if search_username != None:
        users = users.filter(username = search_username.lower())
        li.append(search_username)
    search_fname = request.POST.get('fname', None)
    if search_fname != None:
        users = users.filter(first_name__iexact = search_fname.lower())
        li.append(search_fname)
    search_lname = request.POST.get('lname', None)
    if search_lname != None:
        users = users.filter(last_name__iexact = search_lname.lower())
        li.append(search_lname)
    somme = 0
    for user in users :
        somme += 1
    context = {
        "users": users,
        'userr' : 'clients',
        'somme' : somme,
        'list' : li
    }
    return render(request, 'list_clients.html', context)

@login_required
@user_passes_test(is_admin)

def selectionner_hub(request):
    if request.method == 'POST':
        choice =  request.POST.get('Choices')
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            Product.objects.filter(id=int(idd)).update(checked=True) 
            if idd != '':
                if choice == '0': #delete
                    if idd != '':
                        Product.objects.filter(id=int(idd)).delete()   
                if choice == '3': # suspendre
                    if idd != '':
                        Product.objects.filter(id=int(idd)).update(checked=False) 
                        Product.objects.filter(id=int(idd)).update(suspendus=True)
                        query = Product.objects.get(id=int(idd))
                        email = query.email
                        body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + str(query.id) + " à destination vers " + query.wilaya + ' et envoyé à '+ query.nometpren + " a été suspendu, soit à votre demande, soit à cause d'un problème interne. Vous serez tenu au courant.\nWorld Express vous remercie pour votre confiance."
                        send_mail(
                            'World Express notifications - Colis suspendu',
                            body_text,
                            'from@example.com',
                            [email],
                            fail_silently=False,
                        )
        if choice == "1": #choose delivery                   
            return redirect('choisir_livreurs') 

    return redirect('en_hub_admin')

@login_required
@user_passes_test(is_admin)

def selectionner_transit(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id = idd).update(enhub = True)
                Product.objects.filter(id = idd).update(entransit = False)

    return redirect('transit_admin')
    

@login_required
@user_passes_test(is_admin)

def selectionner_suspendus(request):
    if request.method == 'POST':
        print('here')
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(suspendus=False)
                query = Product.objects.get(id=int(idd))
                email = query.email
                body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + str(query.id) + " à destination vers " + query.wilaya + ' et envoyé à '+ query.nometpren + " n'est plus suspendu.\nWorld Express vous remercie pour votre confiance."
                send_mail(
                    'World Express notifications - arrêt de suspension',
                    body_text,
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
    return redirect('suspendus_admin')

@login_required
@user_passes_test(is_livreur)

def selectionner_livreur_ramassage(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(enramassage=False)
                Product.objects.filter(id=int(idd)).update(enlivraison=True)
    
    return redirect('a_recuperer_livreur')        
"""@login_required
@user_passes_test(is_livreur)

def selectionner_livreur_livraison(request):
    if request.method == 'POST':
        user = request.user
        en_cours_livraison = user.en_cours_livraison
        livres = user.livres
        livres = livres + en_cours_livraison
        idd = user.id
        CustomUser.objects.filter(id = idd).update(en_cours_livraison = '')
        CustomUser.objects.filter(id = idd).update(livres = livres)
        id_list = request.POST.getlist('selection')
        for idd in id_list:
            if idd != '':
                Product.objects.filter(id=int(idd)).update(enlivraison=False)
                query = Product.objects.get(id=int(idd))
                email = query.email
                body_text = 'Bonjour,\nWorld Express vous informe que votre colis numéro ' + str(query.id) + " à destination vers " + query.email + ' et envoyé à '+ query.nometpren + " est bien arrivé.\nWorld Express vous remercie pour votre confiance."
                send_mail(
                    'World Express notifications - Colis arrivé à destination',
                    body_text,
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
    return redirect('en_livraison_livreur')"""

@login_required
@user_passes_test(is_admin)

def choisir_livreur(request):
    users = User.objects.filter(groups__name = 'Livreurs')
    search_username = request.POST.get('username', None)
    li = []
    if search_username != None:
        users = users.filter(username = search_username.lower())
        li.append(search_username)
    search_fname = request.POST.get('fname', None)
    if search_fname != None:
        users = users.filter(first_name__iexact = search_fname.lower())
        li.append(search_fname)
    search_lname = request.POST.get('lname', None)
    if search_lname != None:
        users = users.filter(last_name__iexact = search_lname.lower())
        li.append(search_lname)
    search_disponible = request.POST.get('etat', None)
    if search_disponible == '0':
        users = users.filter(disponible = True)
        li.append(search_disponible)
    if search_disponible == '1':
        users = users.filter(disponible = False)
        li.append(search_disponible)
    search_wilaya = request.POST.get('user_wilaya', None)
    if search_wilaya != '0' and search_wilaya!= None:
        print(search_wilaya)
        users = users.filter(wilaya = search_wilaya)
        li.append(search_wilaya)
    context = {
        "users": users,
        'list' : li
    }
    if request.POST.get('submit', None) != None:
        search_date = request.POST.get('date', None)
        idd = request.POST.get('submit', None)
        search_time = request.POST.get('time', None)
        queryset = Product.objects.filter(checked = True)
        print(queryset)
        s = ''
        compte = 0
        for product in queryset:
            idi = product.id
            Product.objects.filter(id = idi).update(enhub = False)
            Product.objects.filter(id = idi).update(enramassage = True)
            s += ";" + str(product.id)
            compte += 1
        print(s)
        CustomUser.objects.filter(id=int(idd)).update(en_cours_livraison = s)
        if search_date != '' and search_time != '':
            CustomUser.objects.filter(id=int(idd)).update(date = search_date + " " + search_time)
        Product.objects.filter(checked = True).update(checked = False)
        queryset = User.objects.filter(id=idd)
        for query in queryset:
            email = query.email
        body_text = 'Bonjour,\nWorld Express vous informe que vous avez ' + str(compte) + " colis à venir récupérer avant le " + search_date + ' à '+ search_time + '.\nSalutations.'
        send_mail(
            'World Express notifications - Nouveaux Colis',
            body_text,
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return redirect("en_ramassage_admin")
    return render(request, 'choisir_livreurs.html', context)

@login_required
@user_passes_test(is_admin)

def transit_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    email = user.email
    li = []
    queryset = Product.objects.filter(email = email) 
    queryset = Product.objects.filter(entransit = True)
    queryset = queryset.filter(suspendus = False)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        print('aaa',search_type)
        for query in queryset :
            print(query.typeenvoi)
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'en_transit_admin.html',context)


@login_required
@user_passes_test(is_livreur)

def a_recuperer_livreur_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    a = str(user.date).split(' ')
    a1 = a[0].split('-')
    a2 = a[1].split(':')
    date = datetime.datetime(int(a1[0]), int(a1[1]), int(a1[2]), int(a2[0]), int(a2[1]), int(a2[2][:2]))
    a = str(datetime.datetime.now()).split(' ')
    a1 = a[0].split('-')
    a2 = a[1].split(':')
    date2 = datetime.datetime(int(a1[0]), int(a1[1]), int(a1[2]), int(a2[0]), int(a2[1]), int(a2[2][:2]))
    li = []
    retard = ''
    print(user.date)
    print(user.en_cours_livraison)
    print(date2)
    print(date)
    if user.date != '0101-01-01 01:01' and user.en_cours_livraison != '' and date2 >= date :
        retard = 'Vous avez dépassé la deadline : ' + str(user.date) + ' pour récuperer vos colis. Veuillez vous rapprocher des bureaux de World Express dans les plus brefs délais.'
    queryset = Product.objects.filter(nometpren = '')
    a = user.en_cours_livraison
    l = a.split(';')
    for el in l:
        if el != '':
            queryset = queryset.union(Product.objects.filter(id = int(el)).filter(enramassage = True))
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li,
        'retard':retard
    }
    return render(request,'a_recuperer_livreur.html',context)

@login_required
@user_passes_test(is_livreur)
    
def en_livraison_livreur_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    typepresetation = request.POST.get('type de prestation', None)
    user = request.user
    li = []
    queryset = Product.objects.filter(nometpren = '')
    a = user.en_cours_livraison
    l = a.split(';')
    for el in l:
        if el != '':
            queryset = queryset.union(Product.objects.filter(id = int(el)).filter(enlivraison = True))
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(wilaya = search_wilaya) 
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if typepresetation != None and typepresetation != "0":
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(typeprestation = typepresetation) 
        li.append(typepresetation)
    context = {
        "object_list": queryset,
        'list' : li
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
    print(livres)
    li = []
    l = livres.split(';')
    Product.objects.all().order_by('date')
    queryset = Product.objects.filter(nometpren = '')
    for idd in l:
        if idd != '':
            queryset = queryset.union(Product.objects.filter(id = int(idd)).filter(suspendus = False))
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_wilaya)
    if search_date != None and search_date != "":
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_wilaya)
    somme = 0
    for query in queryset:
        somme += 1
    context = {
        "object_list": queryset,
        'list' : li,
        'somme1' : somme
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
    lii = []
    Product.objects.all().order_by('date')
    queryset = Product.objects.filter(pretaexpedier = False).filter(enramassage = False).filter(entransit = False).filter(enhub = False).filter(enlivraison = False).filter(suspendus = False)
    somme = 0
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        lii.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        lii.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        lii.append(search_date)
    if search_date1 != None and search_date2 != None :
        lii.append(search_date1 + ' :: ' + search_date2)
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
                new_queryset = new_queryset.union(el)
        queryset = new_queryset
    if search_price1 != None and search_price2 != 0:
        lii.append(search_price1 + ' :: ' + search_price2)
        new_queryset = queryset
        for el in queryset :
            price = el.payés
            if price >= search_price1 and price <= search_price2:
                new_queryset = new_queryset.union(el)
        queryset = new_queryset
    somme1 = 0
    for el in queryset:
        somme += int(el.payés)
        somme1 += 1
    queryset = queryset.order_by('date')
    context = {
        "object_list": queryset,
        'somme' : somme,
        'somme1': somme1,
        'list' : lii
    }
    return render(request,'historique_admin.html',context)

@login_required
@user_passes_test(is_client)

def historique_client_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    li = []
    Product.objects.all().order_by('date')
    email = request.user.email
    queryset = Product.objects.filter(email = email)
    queryset = queryset.filter(pretaexpedier = False).filter(enramassage = False).filter(entransit = False).filter(enhub = False).filter(enlivraison = False).filter(suspendus = False)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    queryset = queryset.order_by('date')
    somme = 0
    for query in queryset:
        somme += 1
    context = {
        "object_list": queryset,
        'somme1' : somme,
        'list' : li
    }
    return render(request,'historique_client.html',context)

@login_required
@user_passes_test(is_admin)

def en_hub_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    li = []
    queryset = Product.objects.filter(enhub = True) 
    queryset = queryset.filter(suspendus = False)
    l = []
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'en_hub_admin.html',context)

@login_required
@user_passes_test(is_admin)

def en_livraison_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(enlivraison = True) 
    li = []
    queryset = queryset.filter(suspendus = False)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'en_livraison_admin.html',context)

@login_required
@user_passes_test(is_admin)

def en_ramassage_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    type_prestation = request.POST.get('type de prestation', None)
    queryset = Product.objects.filter(enramassage = True) 
    li = []
    queryset = queryset.filter(suspendus = False)
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if type_prestation != '0' and type_prestation!= None:
        queryset = queryset.filter(typeprestation = type_prestation) 
        li.append(type_prestation)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'en_ramassage_admin.html',context)

@login_required
@user_passes_test(is_admin)

def suspendus_admin_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    li = []
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(suspendus = True) 
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya) 
        li.append(search_wilaya) 
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'suspendus_admin.html',context)

@login_required
@user_passes_test(is_client)

def suspendus_client_view(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    li = []
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.filter(suspendus = True) 
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_prestation != None and search_prestation != "0":
        queryset = queryset.filter(typeprestation = search_prestation) 
        li.append(search_prestation)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'suspendus_client.html',context)

@login_required
@user_passes_test(is_livreur)

def livreur_non_payés(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    user = request.user
    li = []
    livres = user.livres
    l = livres.split(';')
    Product.objects.all().order_by('date')
    queryset = Product.objects.filter(nometpren = '')
    for idd in l:
        if idd != '':
            queryset = queryset.union(Product.objects.filter(id = int(idd)).filter(payés = 0))
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(wilaya = search_wilaya) 
        li.append(search_wilaya) 
    if search_type != '0' and search_type != None:
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = Product.objects.filter(id__in=queryset.values('id'))
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'livreur_non_payés.html',context)

@login_required
@user_passes_test(is_admin)

def retour_livreur_admin(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(retour_chez_livreur = True) 
    li = []
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'retour_livreur_admin.html',context)

@login_required
@user_passes_test(is_client)

def payes_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    li = []
    queryset = queryset.exclude(payés = 0)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'payes_client.html',context)

@login_required
@user_passes_test(is_client)

def non_payes_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    queryset = Product.objects.filter(email = request.user.email) 
    li = []
    queryset = queryset.filter(payés = 0)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya) 
        li.append(search_wilaya) 
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'non_payes_client.html',context)

@login_required
@user_passes_test(is_client)

def historique_payements_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    li = []
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.exclude(payés = 0)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya!= None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type)
        li.append(search_type) 
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    somme = 0
    for el in queryset:
        somme += int(el.payés)
    context = {
        "object_list": queryset,
        'somme' : somme,
        'list' : li
    }
    return render(request,'historique_payements_client.html',context)

@login_required
@user_passes_test(is_client)

def retour_livreur_client(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_date = request.POST.get('date', None)
    li = []
    queryset = Product.objects.filter(email = request.user.email) 
    queryset = queryset.filter(retour_chez_livreur = True)
    if search_date != None and search_date != "":
        l = search_date.split('-')
    if search_wilaya != "0" and search_wilaya != None:
        queryset = queryset.filter(wilaya = search_wilaya)  
        li.append(search_wilaya)
    if search_type != '0' and search_type != None:
        queryset = queryset.filter(typeenvoi = search_type) 
        li.append(search_type)
    if search_date != None and search_date != "":
        queryset = queryset.filter(date__contains = datetime.date(int(l[0]),int(l[1]),int(l[2])))
        li.append(search_date)
    context = {
        "object_list": queryset,
        'list' : li
    }
    return render(request,'retour_livreur_client.html',context)

@login_required
@user_passes_test(is_livreur)

def profile_livreur(request):
    user = request.user
    idd = user.id
    new_username = request.POST.get('usernamee',None)
    if new_username != None:
        CustomUser.objects.filter(id = idd).update(username = new_username)
        messages.success(request, 'Your username has been changed successfully')
    context = {
        user : user
    }
    return render(request,'profile_livreur.html',context)

@login_required
@user_passes_test(is_admin)

def profile_admin(request):
    user = request.user
    idd = user.id
    new_username = request.POST.get('usernamee',None)
    if new_username != None:
        CustomUser.objects.filter(id = idd).update(username = new_username)
        messages.success(request, 'Your username has been changed successfully')
    context = {
        user : user
    }
    return render(request,'profile_admin.html',context)

@login_required
@user_passes_test(is_client)

def profile_client(request):
    user = request.user
    idd = user.id
    new_username = request.POST.get('usernamee',None)
    if new_username != None:
        CustomUser.objects.filter(id = idd).update(username = new_username)
        messages.success(request, 'Your username has been changed successfully')
    context = {
        user : user
    }
    return render(request,'profile.html',context)

@login_required
@user_passes_test(is_client)

def add_feedback_client(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.id_user = request.user.id
        obj.save()
        return redirect('client')
    context = {
        'form': form
    }
    return render(request, "add_feedback_client.html", context)

@login_required
@user_passes_test(is_livreur)

def add_feedback_livreur(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.id_user = request.user.id
        obj.save()
        return redirect('livreur')
    context = {
        'form': form
    }
    return render(request, "add_feedback_livreur.html", context)

@login_required
@user_passes_test(is_admin)

def see_feedbacks(request):
    queryset = Feedback.objects.all()
    user_type = request.POST.get('user_type',None)
    l = []
    if user_type != None:
        if user_type == 'not_registrated':
            queryset = Feedback.objects.filter(id_user = -1)
        if user_type == 'client':
            queryset = Feedback.objects.exclude(id_user = -1)
            id_list = []
            for query in queryset:
                id_list.append(int(query.id_user))
            queryset = Feedback.objects.filter(id_user = -2)
            for id in id_list : 
                try:
                    obj = User.objects.get(id = id)
                    if not obj.groups.filter(name = 'Livreurs').exists():
                        queryset = queryset.union(Feedback.objects.filter(id_user = id))
                except:
                    pass
        if user_type == 'livreur':
            queryset = Feedback.objects.exclude(id_user = -1)
            id_list = []
            for query in queryset:
                id_list.append(int(query.id_user))
            queryset = Feedback.objects.filter(id_user = -2)
            for id in id_list : 
                try:
                    obj = User.objects.get(id = id)
                    if obj.groups.filter(name = 'Livreurs').exists():
                        queryset = queryset.union(Feedback.objects.filter(id_user = id))
                except:
                    pass
        l.append(user_type)
    somme = 0
    for query in queryset :
        somme += 1
    context = {
        'object_list' : queryset,
        'somme' : somme,
        'list' : l
    }
    return render(request, "see_feedbacks.html", context)

@login_required
@user_passes_test(is_admin)

def signup_livreur(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname'].lower()
        lname = request.POST['lname'].lower()
        num = request.POST['num']
        wilaya = request.POST['wilaya']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        b = False
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other username.",extra_tags='username')
            b = True
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!",extra_tags='email')
            b = True
        
        if len(str(num)) != 10 or (str(num)[0:2] != '05' and str(num)[0:2] != '06' and str(num)[0:2] != '07' ):
            messages.error(request, "Veuillez saisir un numéro valide",extra_tags='num')
            b = True
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!",extra_tags='username')
            b = True
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!",extra_tags='pass')
            b = True
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!",extra_tags='username')
            b = True
        if b :
            return redirect('signup_livreur.html')
        
        myuser = User.objects.create_user(username=username, email=email)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.num = num
        myuser.wilaya = wilaya
        myuser.set_password(pass1)
        group = Group.objects.get(name='Livreurs')
        myuser.groups.add(group)
        print('here')
        myuser.save()
        
        return redirect("administrateur")
    return render(request, "signup_livreur.html")

@login_required
@user_passes_test(is_admin)

def signup_client(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname'].lower()
        lname = request.POST['lname'].lower()
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        b = False
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other username.",extra_tags='username')
            b = True
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!",extra_tags='email')
            b = True
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!",extra_tags='username')
            b = True
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!",extra_tags='pass')
            b = True
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!",extra_tags='username')
            b = True
        if b :
            return redirect('signup_client.html')
        
        myuser = User.objects.create_user(username=username, email=email)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.set_password(pass1)
        myuser.save()
        
        return redirect("administrateur")
    return render(request, "signup_client.html")


def en_retard_admin(request):
    new_users = User.objects.filter(groups__name = 'Livreurs')
    users = User.objects.filter(username = '')
    for user in new_users :
        a = str(user.date).split(' ')
        a1 = a[0].split('-')
        a2 = a[1].split(':')
        date = datetime.datetime(int(a1[0]), int(a1[1]), int(a1[2]), int(a2[0]), int(a2[1]), int(a2[2][:2]))
        a = str(datetime.datetime.now()).split(' ')
        a1 = a[0].split('-')
        a2 = a[1].split(':')
        date2 = datetime.datetime(int(a1[0]), int(a1[1]), int(a1[2]), int(a2[0]), int(a2[1]), int(a2[2][:2]))
        li = []
        if user.date != '0101-01-01 01:01' and user.en_cours_livraison != '' and date2 >= date :
            users = users.union(User.objects.filter(id = user.id))
    search_username = request.POST.get('username', None)
    search_wilaya = request.POST.get('user_wilaya', None)
    li = []
    if search_username != None:
        users = User.objects.filter(id__in=users.values('id'))
        users = users.filter(username = search_username.lower())
        li.append(search_username)
    search_fname = request.POST.get('fname', None)
    if search_fname != None:
        users = User.objects.filter(id__in=users.values('id'))
        users = users.filter(first_name__iexact = search_fname.lower())
        li.append(search_fname)
    search_lname = request.POST.get('lname', None)
    if search_lname != None:
        users = User.objects.filter(id__in=users.values('id'))
        users = users.filter(last_name__iexact = search_lname.lower())
        li.append(search_lname)
    if search_wilaya != None and search_wilaya != 0:
        users = User.objects.filter(id__in=users.values('id'))
        users = users.filter(wilaya = search_wilaya)
        li.append(search_wilaya)
    somme = 0
    if request.POST.get('submit', None) != None:
        idd = request.POST.get('submit', None)
        users = User.objects.filter(id=idd)
        for user in users:
            email = user.email
            user.delete()
        body_text = "Bonjour,\nWorld Express vous informe que vous venez d'être licensié. Nous nous excusons et vous souhaitons plus de réussites personnelles"
        send_mail(
            'World Express notifications - Licenciement',
            body_text,
            'from@example.com',
            [email],
            fail_silently=False,
        )
        a = user.en_cours_livraison
        l = a.split(';')
        for el in l:
            if el != '':
                Product.objects.filter(id = int(el)).filter(enhub = True)
        return redirect('administrateur')
    if request.POST.get('submit1', None) != None:
        idd = request.POST.get('submit1', None)
        users = User.objects.filter(id=idd)
        for user in users:
            email = user.email
            a = user.en_cours_livraison
            user.delete()
        l = a.split(';')
        for el in l:
            if el != '':
                Product.objects.filter(id = int(el)).filter(enhub = True)
        return redirect('administrateur')
    if request.POST.get('submit2', None) != None:
        idd = request.POST.get('submit2', None)
        users = User.objects.get(id=idd)
        email = user.email
        body_text = "Bonjour,\nWorld Express vous informe que vous avez les colis " + user.en_cours_livraison + " non récupérés en retard. La deadline était pour " + str(user.date) + ' .World Express vous prie de bien venir récupérer les colis dans les plus brefs délais.'
        send_mail(
            'World Express notifications - Colis en retard',
            body_text,
            'from@example.com',
            [email],
            fail_silently=False,
        )
        return redirect('administrateur')
    if request.POST.get('submit3', None) != None:
        idd = request.POST.get('submit3', None)
        user = User.objects.get(id=idd)
        email = user.email
        idd = user.id
        a = user.en_cours_livraison
        CustomUser.objects.filter(id = idd).update(date = '0101-01-01 01:01')
        CustomUser.objects.filter(id = idd).update(en_cours_livraison = "")
        l = a.split(';')
        for el in l:
            if el != '':
                Product.objects.filter(id = int(el)).update(enhub = True)
                Product.objects.filter(id = int(el)).update(enramassage = False)
        return redirect('administrateur')
    for user in users :
        somme += 1
    context = {
        "users": users,
        'list' : li
    }
    return render(request, 'en_retard_admin.html', context)