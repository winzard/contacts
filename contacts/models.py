# coding: UTF-8
from django.db import models
from django_ymap.fields import YmapCoord
from django.utils.translation import ugettext_lazy as _
import re
__author__ = 'winzard'

class ContactQuerySet(models.QuerySet):

    def enabled(self):
        return self.filter(enabled=True).order_by('-priority')

def get_link(phone):
    found = re.findall(r'\d+', phone)
    price_s = ''.join(found)
    return price_s 
    
class Contact(models.Model):
    
    class Meta:
        verbose_name_plural = _('Contacts')
        verbose_name = _('Contact')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255, db_index=True, default='Damage Inc.')
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'), db_index=True)
    address = models.CharField(verbose_name=_('Address'), max_length=255, db_index=True)
    coords = YmapCoord(verbose_name=_('Yandex Map Coordinates'), max_length=255, start_query=u'Россия', size_width=500, size_height=500, db_index=True, blank=True, null=True)
    phone = models.CharField(verbose_name=_('Main Phone Number'), max_length=100, db_index=True)
    email = models.EmailField(verbose_name=_('Main Email'), null=True, blank=True)
    priority = models.IntegerField(verbose_name=_('Priority'), help_text=_('From 10 to 1'), default=0)

    objects = ContactQuerySet.as_manager()

    def __unicode__(self):
        return self.address

    def coords_reversed(self):
        if self.coords:
            return ",".join(self.coords.split(",")[::-1])
        else:
            return None
    
    def get_phone_link(self):
        return get_link(self.phone)
    

class PhoneNumber(models.Model):
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=100, db_index=True)
    comment = models.CharField(verbose_name=_('Comment'), max_length=255, db_index=True, null=True, blank=True)
    contact = models.ForeignKey(Contact, verbose_name=_('Contact'))

    class Meta:
        verbose_name_plural = _('Phone Numbers')
        verbose_name = _('Phone Number')

    def __unicode__(self):
        return u'%s %s' % (self.phone, self.comment)

    def in_international(self):
        return self.phone

    def get_link(self):
        return get_link(self.phone)

class EmailAddress(models.Model):
    email = models.EmailField(verbose_name=_("Email"), db_index=True,)
    comment = models.CharField(verbose_name=_("Comment"), max_length=255, db_index=True, null=True, blank=True)
    contact = models.ForeignKey(Contact, verbose_name=_('Contact'))

    class Meta:
        verbose_name_plural = _("Email")
        verbose_name = _("Emails")

    def __unicode__(self):
        return u'%s %s' % (self.email, self.comment)

class ExtraLink(models.Model):
    ''' Skype, MSN, Telegram, etc'''
    name = models.CharField(verbose_name=_("Name"), max_length=255, db_index=True)
    link = models.CharField(verbose_name=_("Link"), max_length=255, db_index=True)
    comment = models.CharField(verbose_name=_("Comment"), max_length=255, db_index=True, null=True, blank=True)
    contact = models.ForeignKey(Contact, verbose_name=_('Contact'))

    class Meta:
        verbose_name_plural = _("Extra Link")
        verbose_name = _("Extra Links")

    def __unicode__(self):
        return u'%s %s' % (self.name, self.comment)
