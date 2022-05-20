from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def registerview(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.data)
        if form.is_valid():
            print(form.data, "valid")
            form.save
            return redirec('/')
   
    context = {
            'form':form
        }
    return render(request, 'register.html', context=context)
