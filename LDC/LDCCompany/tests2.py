from django.test import TestCase
import unittest
from LDCCompany.forms import AddBUC, AddTar, AddUser, AddRec, AddTC, AddCl
# Create your tests here.

class AddBUCFormTest(TestCase):

    def test_name_label(self):
        form = AddBUC()
        self.assertTrue(form.fields['name_of_copy'].label == None or form.fields['name_of_copy'].label == 'Название копии')

    def test_type_label(self):
        form = AddBUC()
        self.assertTrue(form.fields['type_of_copy'].label == None or form.fields['type_of_copy'].label == 'Тип копии')

    def test_date_label(self):
        form = AddBUC()
        self.assertTrue(form.fields['creation_date'].label == None or form.fields['creation_date'].label == 'Дата создания')

    def test_com_label(self):
        form = AddBUC()
        self.assertTrue(form.fields['commentary'].label == None or form.fields['commentary'].label == 'Комментарий')

    def test_proverka(self):
        form = AddBUC(data={'name_of_copy': "Новая1", 'type_of_copy': "Полная копия", 'creation_date': "2021-01-12", 'commentary': "2"})
        self.assertTrue(form.is_valid())

class AddTarFormTest(TestCase):

    def test_date_label(self):
        form = AddTar()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Дата')

    def test_settlment_label(self):
        form = AddTar()
        self.assertTrue(form.fields['settlment'].label == None or form.fields['settlment'].label == 'Поселение')

    def test_cost_label(self):
        form = AddTar()
        self.assertTrue(form.fields['cost_per_minute'].label == None or form.fields['cost_per_minute'].label == 'Стоимость в минуту')

    def test_preferentialcost_label(self):
        form = AddTar()
        self.assertTrue(form.fields['preferential_cost'].label == None or form.fields['preferential_cost'].label == 'Льготная стоимость (с 20 до 6)')

    def test_proverka(self):
        form = AddTar(data={'date': "2021-01-12", 'settlment': "Карпогоры", 'cost_per_minute': 8, 'preferential_cost': 4})
        self.assertTrue(form.is_valid())

class AddTCFormTest(TestCase):

    def test_date_label(self):
        form = AddTC()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Дата')

    def test_city_label(self):
        form = AddTC()
        self.assertTrue(form.fields['city'].label == None or form.fields['city'].label == 'Город')

    def test_number_label(self):
        form = AddTC()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер телефона')

    def test_callduration_label(self):
        form = AddTC()
        self.assertTrue(form.fields['call_duration'].label == None or form.fields['call_duration'].label == 'Длительность')

    def test_proverka(self):
        form = AddTC(data={'date': "2021-01-12", 'city': "Карпогоры",'number': 270989,'call_duration': 10})
        self.assertTrue(form.is_valid())

class AddClFormTest(TestCase):

    def test_number_label(self):
        form = AddCl()
        self.assertTrue(form.fields['number'].label == None or form.fields['number'].label == 'Номер телефона')

    def test_firstname_label(self):
        form = AddCl()
        self.assertTrue(form.fields['firstname'].label == None or form.fields['firstname'].label == 'Имя')

    def test_lastname_label(self):
        form = AddCl()
        self.assertTrue(form.fields['lastname'].label == None or form.fields['lastname'].label == 'Фамилия')

    def test_address_label(self):
        form = AddCl()
        self.assertTrue(form.fields['address'].label == None or form.fields['address'].label == 'Адрес')

    def test_registrationdate_label(self):
        form = AddCl()
        self.assertTrue(form.fields['registration_date'].label == None or form.fields['registration_date'].label == 'Дата регистрации')

    def test_proverka(self):
        form = AddCl(data={'number': 270989, 'firstname': "Александр", 'lastname': "Станков", 'address': "ул. Папанина 11,кв.21", 'registration_date': "2018-04-12"})
        self.assertTrue(form.is_valid())

class AddRecFormTest(TestCase):

    def test_date_label(self):
        form = AddRec()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Дата')

    def test_cost_label(self):
        form = AddRec()
        self.assertTrue(form.fields['cost'].label == None or form.fields['cost'].label == 'Стоимость')

    def test_term_label(self):
        form = AddRec()
        self.assertTrue(form.fields['payment_term'].label == None or form.fields['payment_term'].label == 'Оплатить до')

    def test_idtariff_label(self):
        form = AddRec()
        self.assertTrue(form.fields['id_tariff'].label == None or form.fields['id_tariff'].label == 'Номер тарифа')

    def test_idtconversation_label(self):
        form = AddRec()
        self.assertTrue(form.fields['id_tconversation'].label == None or form.fields['id_tconversation'].label == 'Номер разговора')

    def test_idclient_label(self):
        form = AddRec()
        self.assertTrue(form.fields['id_client'].label == None or form.fields['id_client'].label == 'Номер клиента')

    def test_proverka(self):
        form = AddRec(data={'date': "2021-01-12", 'cost': "80", 'payment_term': "2021-02-01", 'id_tariff': 1, 'id_tconversation': 1, 'id_client': 1})
        self.assertTrue(form.is_valid())

class AddUserFormTest(TestCase):

    def test_login_label(self):
        form = AddUser()
        self.assertTrue(form.fields['login'].label == None or form.fields['login'].label == 'Логин')

    def test_password_label(self):
        form = AddUser()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Пароль')

    def test_idreceipt_label(self):
        form = AddUser()
        self.assertTrue(form.fields['id_receipt'].label == None or form.fields['id_receipt'].label == 'Номер квитанции')

    def test_idclient_label(self):
        form = AddUser()
        self.assertTrue(form.fields['id_client'].label == None or form.fields['id_client'].label == 'Номер клиента')

    def test_proverka(self):
        form = AddUser(data={'login': 270989, 'password': "2015Ah7Jjm8k", 'id_receipt': 1, 'id_client': 1})
        self.assertTrue(form.is_valid())