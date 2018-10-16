from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect("main:landing")
        else:
            return render(request, 'main/home.html', {'error_message': 'Invalid login'})
    else:
        if request.user.is_authenticated is True:
            return render(request, 'main/landing.html')
        elif request.GET.get('next'):
            return render(request, 'main/home.html', {'error_message': 'You must log in to see this page' })
        return render(request, 'main/home.html')

def logout_user(request):
    logout(request)
    return redirect('main:home')
    
def landing(request):
    return render(request, 'main/landing.html')
# Create your views here.
