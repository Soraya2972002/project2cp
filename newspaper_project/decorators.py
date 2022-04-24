

def is_client(user):
    return not user.groups.filter(name='Livreurs').exists() and not user.groups.filter(name='admin_wilaya').exists()
def is_adminwilaya(user):
    return user.groups.filter(name='admin_wilaya').exists()
def is_livreur(user):
    return user.groups.filter(name='Livreurs').exists()
def is_admin(user):
    return user.is_superuser