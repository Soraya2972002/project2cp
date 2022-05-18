from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True
        #self.fields['num'].required = True

class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'wilaya','num','disponible',"en_cours_livraison","date",
        )
    exclude = ['Important dates',]
    fieldsets = (
        (None, {
            'fields': ('username',),'classes': ('wide',)
        }),
        ('Permissions', {
            'fields': (
                'groups',
                )
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','num'),
        }),
        ('Additional info', {
            'fields': ('wilaya',)
        })
    )
    """('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),"""
        #needs to be added lfo9 w lta7t
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2'),'classes': ('wide',)
        }),
        ('Permissions', {
            'fields': (
                'groups',
                )
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','num')
        }),
        ('Additional info', {
            'fields': ('wilaya',)
        })
        
    )
    
    search_fields = ('username',)
    form = UserChangeForm
    add_form = UserCreationForm

admin.site.register(CustomUser, CustomUserAdmin)
