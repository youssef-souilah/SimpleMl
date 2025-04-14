from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count

from App.views import Train,Image
# Create your views here.

def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin)
@login_required
def dashboard(request):
    return render(request,"views/dashboard.html")


@user_passes_test(is_admin)
@login_required
def user_list_view(request):
    users = User.objects.all()
    return render(request, 'views/users.html', {'users': users})



@user_passes_test(is_admin)
@login_required
def trains_view(request):
    trains = Train.objects.select_related('user').annotate(image_count=Count('images'))
    return render(request, 'views/trains.html', {'trains': trains})



@user_passes_test(is_admin)
@login_required
def images_usage_view(request):
    images = Image.objects.annotate(train_count=Count('trains'))
    return render(request, 'views/images.html', {'images': images})

