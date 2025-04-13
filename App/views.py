from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Image , Train
from django.contrib.auth.decorators import login_required, user_passes_test
import os
import random
# Create your views here.
def index(request):
    return render(request,"views/index.html")


def get_images():
    images_grouped_by_type = Image.objects.all().order_by('type')

    images_by_type = {}
    for image in images_grouped_by_type:
        if image.type not in images_by_type:
            images_by_type[image.type] = []
        images_by_type[image.type].append(image)
    return images_by_type


def classify(img):
    score = 50
    label = "cat"
    for label_key, image_list in get_images().items():
        if label_key in img.name:
            label = label_key
            for image_name in image_list:
                if image_name.name == img.name:
                    score = random.randint(85, 99)
                    return label, score
            score = random.randint(60, 80)
            return label, score
    return label, score


# def is_admin(user):
#     return user.is_staff


# @user_passes_test(is_admin)
@login_required
def test(request):
    if request.method=="POST":
        img=request.FILES.get('img')
        
        label , score=classify(img)
        
        return JsonResponse({
            'message':"success",
            'score':score,
            'label':label
        })
    return render(request,"views/insert.html",{
        'data':get_images(),
        'user':request.user,
    })
    
    
@login_required 
def app(request):
    if request.method == "POST":
        cats = request.FILES.getlist('cats[]')
        dogs = request.FILES.getlist('dogs[]')
        train = Train.objects.create(
            user=request.user
        )
        for img in cats:
            original_name = os.path.basename(img.name)
            image="" 
            if Image.objects.filter(name=original_name).exists():
                image = Image.objects.get(name=original_name)
            else:
                image=Image.objects.create(image=img, name=original_name,type="cat")
            train.images.add(image)   
        for img in dogs:
            original_name = os.path.basename(img.name) 
            image =""
            if Image.objects.filter(name=original_name).exists():
                image = Image.objects.get(name=original_name)
            else:
                image = Image.objects.create(image=img, name=original_name,type="dog")
            train.images.add(image)
        return JsonResponse({
            'message':"success"
        })

    return render(request, "views/test.html", {
        'data': get_images(),
        'user':request.user,
    })