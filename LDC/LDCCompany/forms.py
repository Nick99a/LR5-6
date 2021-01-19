from django import forms

class AddBUC(forms.Form):
    name_of_copy = forms.CharField(label="Название копии")
    type_of_copy = forms.CharField(label="Тип копии")
    creation_date = forms.DateField(label="Дата создания")
    commentary = forms.CharField(label="Комментарий")

class AddTar(forms.Form):
    date = forms.DateField(label="Дата")
    settlment = forms.CharField(label="Поселение")
    cost_per_minute = forms.FloatField(label="Стоимость в минуту")
    preferential_cost = forms.FloatField(label="Льготная стоимость (с 20 до 6)")

class AddRec(forms.Form):
    date = forms.DateField(label="Дата")
    cost = forms.FloatField(label="Стоимость")
    payment_term = forms.DateField(label="Оплатить до")
    id_tariff = forms.IntegerField(label="Номер тарифа")
    id_tconversation = forms.IntegerField(label="Номер разговора")
    id_client = forms.IntegerField(label="Номер клиента")

class AddTC(forms.Form):
    date = forms.DateField(label="Дата")
    city = forms.CharField(label="Город")
    number = forms.CharField(label="Номер телефона")
    call_duration = forms.FloatField(label="Длительность")

class AddCl(forms.Form):
    number = forms.CharField(label="Номер телефона")
    firstname = forms.CharField(label="Имя")
    lastname = forms.CharField(label="Фамилия")
    address = forms.CharField(label="Адрес")
    registration_date = forms.DateField(label="Дата регистрации")

class AddUser(forms.Form):
    login = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль")
    id_receipt = forms.IntegerField(label="Номер квитанции")
    id_client = forms.IntegerField(label="Номер клиента")

