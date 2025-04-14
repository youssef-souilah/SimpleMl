from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin)
@login_required
def dashboard(request):
    return render(request,"views/dashboard.html")

