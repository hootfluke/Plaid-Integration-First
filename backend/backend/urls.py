"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from form import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-user/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('token-exchange/', views.TokenExchange.as_view(), name="token-exchange"),
    path('get-transactions/', views.GetTransactions.as_view(), name="transactions"),
    path('get-accounts/', views.GetAccounts.as_view(), name="account"),
    path('update-transaction/', views.TransactionUpdate.as_view(), name="update-transaction-hook"),
    ]
