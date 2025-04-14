from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from App.views import Train,Image
# Create your views here.

def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin)
@login_required
def dashboard(request):
    today = timezone.now()
    last_month = today - timedelta(days=30)

    # Counts
    total_users = User.objects.count()
    total_trains = Train.objects.count()
    total_datasets = Image.objects.count()
    total_images_used = Train.objects.values('images').distinct().count()

    # Growth % from last month
    users_last_month = User.objects.filter(date_joined__gte=last_month).count()
    trains_last_month = Train.objects.filter(created_at__gte=last_month).count()
    datasets_last_month = Image.objects.filter(created_at__gte=last_month).count()  # If you store created_at
    used_images_last_month = Train.objects.filter(created_at__gte=last_month).values('images').distinct().count()

    top_trains = Train.objects.select_related('user') \
                             .annotate(image_count=Count('images')) \
                             .order_by('-image_count')[:10]
    
    def get_growth(current, last):
        if last == 0:
            return 100.0 if current > 0 else 0.0
        return round(((current - last) / last) * 100, 1)

    context = {
        "total_users": total_users,
        "total_trains": total_trains,
        "total_datasets": total_datasets,
        "total_images_used": total_images_used,

        "users_growth": get_growth(total_users, total_users - users_last_month),
        "trains_growth": get_growth(total_trains, total_trains - trains_last_month),
        "datasets_growth": get_growth(total_datasets, total_datasets - datasets_last_month),
        "images_used_growth": get_growth(total_images_used, total_images_used - used_images_last_month),
        "top_trains": top_trains,
    }
    return render(request,"views/dashboard.html",context)


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

