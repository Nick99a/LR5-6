from django.test import TestCase
import unittest
from LDCCompany.models import BackUpCopy, Tariff, Receipt, TelephoneConversation, Client, User
# Create your tests here.

class BackUpCopyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        BackUpCopy.objects.create(name_of_copy='Новая', type_of_copy='Полная', creation_date='2021-01-10', commentary='Тестовый')

    def test_name_label(self):
        copy=BackUpCopy.objects.get(id=1)
        field_label = copy._meta.get_field('name_of_copy').verbose_name
        self.assertEquals(field_label,'name of copy')

    def test_type_label(self):
        copy=BackUpCopy.objects.get(id=1)
        field_label = copy._meta.get_field('type_of_copy').verbose_name
        self.assertEquals(field_label,'type of copy')

    def test_creationdate_label(self):
        copy=BackUpCopy.objects.get(id=1)
        field_label = copy._meta.get_field('creation_date').verbose_name
        self.assertEquals(field_label,'creation date')

    def test_commentary_label(self):
        copy=BackUpCopy.objects.get(id=1)
        field_label = copy._meta.get_field('commentary').verbose_name
        self.assertEquals(field_label,'commentary')

    def test_type_max_length(self):
        copy=BackUpCopy.objects.get(id=1)
        max_length = copy._meta.get_field('type_of_copy').max_length
        self.assertEquals(max_length,45)

    def test_name_max_length(self):
        copy=BackUpCopy.objects.get(id=1)
        max_length = copy._meta.get_field('name_of_copy').max_length
        self.assertEquals(max_length,45)

    def test_commentary_max_length(self):
        copy=BackUpCopy.objects.get(id=1)
        max_length = copy._meta.get_field('commentary').max_length
        self.assertEquals(max_length,100)

class TariffModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Tariff.objects.create(date='2021-01-11', settlment='Москва', cost_per_minute=35, preferential_cost=20)

    def test_date_label(self):
        tar=Tariff.objects.get(id=1)
        field_label = tar._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'date')

    def test_settlment_label(self):
        tar=Tariff.objects.get(id=1)
        field_label = tar._meta.get_field('settlment').verbose_name
        self.assertEquals(field_label,'settlment')

    def test_costperminute_label(self):
        tar=Tariff.objects.get(id=1)
        field_label = tar._meta.get_field('cost_per_minute').verbose_name
        self.assertEquals(field_label,'cost per minute')

    def test_name_label(self):
        tar=Tariff.objects.get(id=1)
        field_label = tar._meta.get_field('preferential_cost').verbose_name
        self.assertEquals(field_label,'preferential cost')

    def test_settlment_max_length(self):
        tar=Tariff.objects.get(id=1)
        max_length = tar._meta.get_field('settlment').max_length
        self.assertEquals(max_length,45)

class TelephoneConversationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        TelephoneConversation.objects.create(date='2021-01-11', city='Москва', number='782563', call_duration=3)

    def test_date_label(self):
        conv=TelephoneConversation.objects.get(id=1)
        field_label = conv._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'date')

    def test_city_label(self):
        conv=TelephoneConversation.objects.get(id=1)
        field_label = conv._meta.get_field('city').verbose_name
        self.assertEquals(field_label,'city')

    def test_number_label(self):
        conv=TelephoneConversation.objects.get(id=1)
        field_label = conv._meta.get_field('number').verbose_name
        self.assertEquals(field_label,'number')

    def test_callduration_label(self):
        conv=TelephoneConversation.objects.get(id=1)
        field_label = conv._meta.get_field('call_duration').verbose_name
        self.assertEquals(field_label,'call duration')

    def test_city_max_length(self):
        conv=TelephoneConversation.objects.get(id=1)
        max_length = conv._meta.get_field('city').max_length
        self.assertEquals(max_length,45)

    def test_number_max_length(self):
        conv=TelephoneConversation.objects.get(id=1)
        max_length = conv._meta.get_field('number').max_length
        self.assertEquals(max_length,45)

class ReceiptModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Receipt.objects.create(date='2021-01-11', cost=105, payment_term='2021-02-05')

    def test_date_label(self):
        rec=Receipt.objects.get(id=1)
        field_label = rec._meta.get_field('date').verbose_name
        self.assertEquals(field_label,'date')

    def test_cost_label(self):
        rec=Receipt.objects.get(id=1)
        field_label = rec._meta.get_field('cost').verbose_name
        self.assertEquals(field_label,'cost')

    def test_paymentterm_label(self):
        rec=Receipt.objects.get(id=1)
        field_label = rec._meta.get_field('payment_term').verbose_name
        self.assertEquals(field_label,'payment term')

class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Client.objects.create(number='782563', firstname='Владислав', lastname='Задорный', address='ул. Карла Маркса 12, кв. 25', registration_date='2021-01-11')

    def test_number_label(self):
        cl=Client.objects.get(id=1)
        field_label = cl._meta.get_field('number').verbose_name
        self.assertEquals(field_label,'number')

    def test_firstname_label(self):
        cl=Client.objects.get(id=1)
        field_label = cl._meta.get_field('firstname').verbose_name
        self.assertEquals(field_label,'firstname')

    def test_lastname_label(self):
        cl=Client.objects.get(id=1)
        field_label = cl._meta.get_field('lastname').verbose_name
        self.assertEquals(field_label,'lastname')

    def test_lastname_label(self):
        cl=Client.objects.get(id=1)
        field_label = cl._meta.get_field('address').verbose_name
        self.assertEquals(field_label,'address')

    def test_registrationdate_label(self):
        cl=Client.objects.get(id=1)
        field_label = cl._meta.get_field('registration_date').verbose_name
        self.assertEquals(field_label,'registration date')

    def test_number_max_length(self):
        cl=Client.objects.get(id=1)
        max_length = cl._meta.get_field('number').max_length
        self.assertEquals(max_length,45)

    def test_firstname_max_length(self):
        cl=Client.objects.get(id=1)
        max_length = cl._meta.get_field('firstname').max_length
        self.assertEquals(max_length,45)

    def test_lastname_max_length(self):
        cl=Client.objects.get(id=1)
        max_length = cl._meta.get_field('lastname').max_length
        self.assertEquals(max_length,45)

    def test_address_max_length(self):
        cl=Client.objects.get(id=1)
        max_length = cl._meta.get_field('address').max_length
        self.assertEquals(max_length,45)

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(login='782563', password='Th34m20Cd')

    def test_login_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('login').verbose_name
        self.assertEquals(field_label,'login')

    def test_phone_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label,'password')

    def test_name_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('login').max_length
        self.assertEquals(max_length,45)

    def test_birthday_max_length(self):
        user=User.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length,45)

