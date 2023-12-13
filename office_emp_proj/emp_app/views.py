from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_emp(request):
    if request.method == "POST":
        employee_data = {
            'firstName': request.POST['firstName'],
            'lastName': request.POST['lastName'],
            'dept_id': int(request.POST['dept']),
            'salary': int(request.POST['salary']),
            'bonus': int(request.POST['bonus']),
            'role_id': int(request.POST['role']),
            'phone': int(request.POST['phone']),
            'dateOfJoining': datetime.now(),
        }
        print(employee_data)
        new_user = Employee(**employee_data)
        new_user.save()
        return HttpResponse("Employee Added successfully")
    else:
        return render(request, 'add_emp.html')

def remove_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def remove_emp_id(request, emp_id=0):
    delete_emp = Employee.objects.get(id=emp_id)
    delete_emp.delete()
    return HttpResponse("Employee Removed successfully")
    
def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view_emp.html', context)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        print(name)
        print(dept)
        print(role)
        if name:
            emps = emps.filter(Q(firstName__icontains = name) | Q(lastName__icontains = name))            
        if dept:
            emps = emps.filter(dept__name__icontains = dept)            
        if role:
            emps = emps.filter(drole__name__icontains = role)   
        context = {
            'emps': emps
        }         
        return render(request, 'view_emp.html', context)
    else:
        return render(request, 'filter_emp.html')
