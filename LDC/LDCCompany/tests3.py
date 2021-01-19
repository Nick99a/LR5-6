from django.test import TestCase
import unittest
from LDCCompany.models import BackUpCopy, Tariff, Receipt, TelephoneConversation, Client, User
# Create your tests here.
from django.urls import reverse
from LDCCompany.forms import AddBUC, AddTar, AddUser, AddRec, AddTC, AddCl

class BackUpCopyViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        BackUpCopy.objects.create(name_of_copy='Новая', type_of_copy='Полная', creation_date='2021-01-10', commentary='Тестовый')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/backup/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('backup'))
        self.assertEqual(resp.status_code, 200)


    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('backup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'LDCCompany/Template_BackUp.html')

class TariffViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tariff.objects.create(date='2021-01-11', settlment='Москва', cost_per_minute=35, preferential_cost=20)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/tariff/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('tariff'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('tariff'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'LDCCompany/Template_Tariff.html')

class TelephoneConversationViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TelephoneConversation.objects.create(date='2021-01-11', city='Москва', number='782563', call_duration=3)

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/conversation/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('conversation'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('conversation'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'LDCCompany/Template_Conversation.html')

class ClientViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Client.objects.create(number='782563', firstname='Владислав', lastname='Задорный', address='ул. Карла Маркса 12, кв. 25', registration_date='2021-01-11')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/client/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('client'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('client'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'LDCCompany/Template_Client.html')

class ReceiptViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Receipt.objects.create(date='2021-01-11', cost=105, payment_term='2021-02-05')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/receipt/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('receipt'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('receipt'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'LDCCompany/Template_Receipt.html')

class UserViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(login='782563', password='Th34m20Cd')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/user/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'LDCCompany/Template_User.html')

class AnotherViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(login='782563', password='Th34m20Cd')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/user/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_view_url_exists_at_desired_location1(self): # существование url по адресу
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name1(self): # существование url по имени
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template1(self): # соответствие шаблону
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'great.html')

