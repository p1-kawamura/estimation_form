from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index,shouhin_add_up,shouhin_modal_up,shouhin_del,print_add_up,print_modal_up,print_del,btn_submit, \
                    list_index,est_detail

app_name="est"
urlpatterns = [
    path('', index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='estimation/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('shouhin_add_up/', shouhin_add_up, name="shouhin_add_up"),
    path('shouhin_modal_up/', shouhin_modal_up, name="shouhin_modal_up"),
    path('shouhin_del/', shouhin_del, name="shouhin_del"),
    path('print_add_up/', print_add_up, name="print_add_up"),
    path('print_modal_up/', print_modal_up, name="print_modal_up"),
    path('print_del/', print_del, name="print_del"),
    path('btn_submit/', btn_submit, name="btn_submit"),
    path('list_index/', list_index, name="list_index"),
    path('est_detail/<int:est_num>', est_detail, name="est_detail"),
]