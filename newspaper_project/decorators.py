#User.objects.filter(groups__name = None)

def is_client(user):
    #return not user.groups.filter(name='Livreurs').exists() and not user.is_superuser
    return True
def is_adminwilaya(user):
    #return user.groups.filter(name='admin_wilaya').exists()
    return True
def is_livreur(user):
    #return user.groups.filter(name='Livreurs').exists()
    return True
def is_admin(user):
    #return user.is_superuser
    return True