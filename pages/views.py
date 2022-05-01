from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required

from newspaper_project.decorators import is_admin, is_adminwilaya, is_client, is_livreur

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
    return render(request,'client.html',{})
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
    return render(request,'En_ramassage.html',{})
@login_required
@user_passes_test(is_client)
def transit_view(request, *args, **kwargs):
    return render(request,'En_transit.html',{})
@login_required
@user_passes_test(is_client)
def livraison_view(request, *args, **kwargs):
    return render(request,'En-livraison.html',{})
@login_required
@user_passes_test(is_client)
def non_encaisse_view(request, *args, **kwargs):
    return render(request,'Non_encaisse.html',{})
@login_required
@user_passes_test(is_client)
def pret_a_expedier_view(request, *args, **kwargs):
    return render(request,'pret-a-expedier.html',{})
@login_required
@user_passes_test(is_client)
def suspendus_view(request, *args, **kwargs):
    return render(request,'Suspendus.html',{})
@login_required
@user_passes_test(is_client)
def hub_view(request, *args, **kwargs):
    return render(request,'En_hub.html',{})