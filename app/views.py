from django.shortcuts import redirect,render
from app.forms import Emp_form
from app.models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
@login_required
def home(request):
    emp=Employee.objects.all()
    return render(request,'app/home.html',{'emp':emp})
@login_required
def detail(request,id):
    emp1=Employee.objects.get(id=id)
    return render(request,'app/employee_detail.html',{'emp1':emp1})
@login_required
def add_emp(request):
    if request.method =='POST':
        form =Emp_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_success')
    else:
       form=Emp_form()
    return render(request,'app/add_employee.html',{'form':form})
@login_required
def success_view(request):
    return render(request,'app/success.html')
def register(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
       form.save()
       return redirect('login')
  else:
       form=UserCreationForm()
  return render(request,'app/register.html',{'form':form})

   