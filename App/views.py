from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Image
import os
# Create your views here.
def index(request):
    return render(request,"views/index.html")


def get_images():
    images_grouped_by_type = Image.objects.all().order_by('type')
    # Loop through grouped images and filter by type
    images_by_type = {}
    for image in images_grouped_by_type:
        if image.type not in images_by_type:
            images_by_type[image.type] = []
        images_by_type[image.type].append(image)
    return images_by_type

def test(request):
    if request.method=="POST":
        img=request.FILES.get('img')
        # print(os.path.basename(img.name))
        print(img)
        print(get_images())
        return JsonResponse({
            'message':"success"
        })
    return render(request,"views/insert.html",{
        'data':get_images(),
    })
    
    
    
def app(request):
    if request.method == "POST":
        cats = request.FILES.getlist('cats[]')
        dogs = request.FILES.getlist('dogs[]')
        for img in cats:
            original_name = os.path.basename(img.name) 
            if Image.objects.filter(name=original_name).exists():
                continue  
            Image.objects.create(image=img, name=original_name,type="cat")
        for img in dogs:
            original_name = os.path.basename(img.name) 
            if Image.objects.filter(name=original_name).exists():
                continue  
            Image.objects.create(image=img, name=original_name,type="dog")
            
        return JsonResponse({
            'message':"success"
        })

    return render(request, "views/test.html", {'data': get_images()})