from contacts.models import get_link

__author__ = 'winzard'
from django.test import TestCase

class ContactTest(TestCase):


    def test_phone_number(self):
        phones = ['+7 999 434 23 44', '+7 (999) 434 23 44', '+7 (999) 434-23-44', '+7999 434 23-44']
        for p in phones:
            assert '79994342344' == get_link(p)




class PhoneNumberTest(TestCase):
    pass

class EmailAddressTest(TestCase):
    pass
