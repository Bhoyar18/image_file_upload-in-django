from django.shortcuts import render
from .models import*
from .forms import*


# Create your views here.
def home(request):
    form = StudentForm()
    msg = " Fill Registration Form "
    if request.method=="POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg = "Registered successfully"
        else:
            msg = "Please enter the fields correctly"    

    data = Student.objects.all()
    return render(request,'home.html',{'form':form,'data':data,'msg':msg})

def showdata(request):
    data1 = Student.objects.all()
    data = data1.values()
    return render(request,'show.html',{'data':data})


