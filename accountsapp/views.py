from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect 
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required





def signup(request):
    template_data={}
    template_data['title']='Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accountsapp/signup.html', {'template_data': template_data})
    
    
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accountsapp.login')
        else:
            template_data['form'] = form
            return render(request, 'accountsapp/signup.html', {'template_data': template_data})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('homeapp.index')


def login(request):
    template_data={}
    template_data['title']='Login'
    if request.method == 'GET':
        return render(request, 'accountsapp/login.html', {'template_data': template_data})
    
    
    
    elif request.method == 'POST':
        user = authenticate(
            request,        
            username = request.POST['username'],
            password = request.POST['password']
        )
        
        if user is None:
            template_data['error'] = 'Invalid username or password'
            return render('accountsapp/login.html', {'template_data':template_data})
        else:
            auth_login(request, user) 
            return redirect( 'homeapp.index')
        
        

@login_required
def orders(request):
     template_data={}
     template_data['title']='Orders'    
     template_data['orders'] = request.user.order_set.all()
     return render(request,'accountsapp/orders.html', {'template_data':template_data})
 
 
 
 
         
        