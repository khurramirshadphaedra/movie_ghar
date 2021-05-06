from django.urls import path
from account.views import home, login_view, logout_view, account_view, registration_view
from account import views
urlpatterns = [
    path('register', registration_view, name="register"),
    path('logout', logout_view, name="logout"),
    path('login', login_view, name="login"),
    path('', views.home, name="home"),
    path('profile', account_view, name="account"),
    path('show/', views.show, name="show"),
    path('show/delete/<int:userid>', views.delete, name="delete"),
    path('show/edit/<int:userid>', views.edit, name="edit"),
    path('show/edit/update/<int:userid>', views.update, name="update"),

]
