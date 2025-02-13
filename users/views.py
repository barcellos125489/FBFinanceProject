from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Logs out the already authenticated user"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signin(request):
    """Creates a new instance of users in FBFinance_DB"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    
    context = {'form': form}
    return render(request, 'users/signin.html', context)




# def login(request):
#     return render(request, 'users/login.html')

# Create your views here.
