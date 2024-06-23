from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from app.forms import * 
def Product_view(request):
    PFO=ProductForm() 
    d={'PFO':PFO}
    if request.method=='POST':
        PDFO=ProductForm(request.POST)
        if PDFO.is_valid():
            PDFO.save()
            return HttpResponseRedirect(reverse('view_products'))
        
        
    return render(request,'products.html',d)
def view_products(request):
    PQO=Product.objects.all()
    d={'PQO':PQO}
    return render(request,'productlist.html',d)
def update_product(request,val):
    PQO=Product.objects.get(pk=val)
    PFO=ProductForm()
    d={'PFO':PFO}
    if request.method=='POST':
         PQDO=ProductForm(request.POST,instance=PQO)
         if PQDO.is_valid():
             PQDO.save()
             return HttpResponseRedirect(reverse('view_products'))
    return render(request,'products.html',d)
def delete_product(request,val):
    PQO=Product.objects.get(product_id=val)
    PQO.delete()
    return HttpResponseRedirect(reverse('view_products'))
def Emp_view(request):
    EFO=EmpForm() 
    d={'EFO':EFO}
    if request.method=='POST':
        EDFO=EmpForm(request.POST)
        if EDFO.is_valid():
            EDFO.save()
            return HttpResponseRedirect(reverse('view_employees'))
           
        
    return render(request,'emp.html',d)
def view_employees(request):
    EQO=Employee.objects.all()
    d={'EQO':EQO}
    return render(request,'Employeelist.html',d)
def update_employee(request,val):
    EQO=Employee.objects.get(emp_id=val)
    EFO=EmpForm()
    d={'EFO':EFO}
    if request.method=='POST':
         EQDO=EmpForm(request.POST,instance=EQO)
         if EQDO.is_valid():
             EQDO.save()
             return HttpResponseRedirect(reverse('view_employees'))
    return render(request,'emp.html',d)
def delete_employee(request,val):
    EQO=Employee.objects.get(emp_id=val)
    EQO.delete()
    return HttpResponseRedirect(reverse('view_employees'))
def profit_and_loss(request):
    total_revenue = sum(product.price * product.quantity for product in Product.objects.all())
    total_salary = sum(employee.salary for employee in Employee.objects.all())
    profit_loss = total_revenue - total_salary
    return HttpResponse(f'profit and loss{profit_loss}')