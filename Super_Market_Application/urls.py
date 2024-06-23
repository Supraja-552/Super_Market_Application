"""
URL configuration for Super_Market_Application project.

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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Product_view/',Product_view,name='Product_view'),
    path('view_products/',view_products,name='view_products'),
    path('update_product/<int:val>/',update_product,name='update_product')
    , path('delete_product/<int:val>/',delete_product,name='delete_product'),
    path('Emp_view/',Emp_view,name='Emp_view'),
        path('view_employees/',view_employees,name='view_employees'),
        path('update_employee/<int:val>/',update_employee,name='update_employee')
    , path('delete_employee/<int:val>/',delete_employee,name='delete_employee'),
    path('profit_and_loss/',profit_and_loss,name='profit_and_loss'),
]
