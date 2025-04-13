from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  user_passes_test
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

def not_authenticated(user):
    return not user.is_authenticated

@user_passes_test(not_authenticated, login_url='/')
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
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')  # or redirect_user(request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return redirect_user(self.request.user).url

# Redirection Logic
def redirect_user(user):
    if user.is_staff:
        return redirect('/dashboard')  
    return redirect('/app')          
