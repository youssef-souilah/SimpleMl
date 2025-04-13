from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Register View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False 
            user.save()
            login(request, user)
            return redirect_user(user)
    else:
        form = UserCreationForm()
    return render(request, 'views/register.html', {'form': form})

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'views/login.html'

    def get_success_url(self):
        return redirect_user(self.request.user).url

# Redirection Logic
def redirect_user(user):
    if user.is_staff:
        return redirect('/dashboard/')  
    return redirect('/app/')          
