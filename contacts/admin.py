from django.contrib import admin
from django_ymap.admin import YmapAdmin
from contacts.models import PhoneNumber, EmailAddress, ExtraLink, Contact, ContactGroup

__author__ = 'winzard'
class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1

class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    extra = 1

class ExtraLinkInline(admin.TabularInline):
    model = ExtraLink
    extra = 1

class ContactAdmin(YmapAdmin, admin.ModelAdmin):
    inlines = [PhoneNumberInline, EmailAddressInline, ExtraLinkInline]

admin.site.register(Contact, ContactAdmin)


class ContactGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ['contacts']


admin.site.register(ContactGroup, ContactGroupAdmin)