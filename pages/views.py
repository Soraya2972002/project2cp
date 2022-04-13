from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>This is the home page</h1>")
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

def user_view(request, *args, **kwargs):
    return render(request,'client.html',{})

def admin_view(request, *args, **kwargs):
    return render(request,'admin.html',{})

def admin_view(request, *args, **kwargs):
    return render(request,'admin_wilaya_view.html',{})


def livreur_view(request, *args, **kwargs):
    return render(request,'livreurs.html',{})