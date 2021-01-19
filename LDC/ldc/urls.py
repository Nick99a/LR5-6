
from django.contrib import admin
from django.urls import path
from LDCCompany import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()



urlpatterns = [
    path('',views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('ldc/', views.index, name='home'),
    path('backup/', views.index_backup, name='backup'),
    path('user/', views.index_user, name='user'),
    path('tariff/', views.index_tariff, name='tariff'),
    path('receipt/', views.index_receipt, name='receipt'),
    path('conversation/', views.index_telephone_conversation, name='conversation'),
    path('client/', views.index_client, name='client'),
    path('backup/add/', views.view_backup.add_backup, name='add_backup'),
    path("backup/del/", views.view_backup.del_backup, name="del_backup"),
    path("backup/up/", views.view_backup.update_backup, name="update_backup"),
    path('user/addu/', views.view_user.add_user, name='add_user'),
    path("user/delu/", views.view_user.del_user, name="del_user"),
    path("user/upu/", views.view_user.update_user, name="update_user"),
    path('tariff/addt/', views.view_tariff.add_tariff, name='add_tariff'),
    path("tariff/delt/", views.view_tariff.del_tariff, name="del_tariff"),
    path("tariff/upt/", views.view_tariff.update_tariff, name="update_tariff"),
    path('receipt/addr/', views.view_receipt.add_receipt, name='add_receipt'),
    path("receipt/delr/", views.view_receipt.del_receipt, name="del_receipt"),
    path("receipt/upr", views.view_receipt.update_receipt, name="update_receipt"),
    path('conversation/addc/', views.view_conversation.add_conversation, name='add_conversation'),
    path("conversation/delc/", views.view_conversation.del_conversation, name="del_conversation"),
    path("conversation/upc/", views.view_conversation.update_conversation, name="update_conversation"),
    path('client/addcl/', views.view_client.add_client, name='add_client'),
    path("client/delcl/", views.view_client.del_client, name="del_client"),
    path("client/upcl/", views.view_client.update_client, name="update_client"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]