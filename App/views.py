from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
import os
# Create your views here.
def index(request):
    return render(request,"views/index.html")
data={
        'cats':[
            '/static/images/cats/cat1.jpeg',
            '/static/images/cats/cat2.jpeg',
            '/static/images/cats/cat3.jpeg',
            '/static/images/cats/cat4.jpeg',
            '/static/images/cats/cat5.jpeg',
            '/static/images/cats/cat6.jpeg',
            '/static/images/cats/cat7.jpeg',
            '/static/images/cats/cat8.jpeg',
            '/static/images/cats/cat9.jpeg',
            '/static/images/cats/cat10.jpeg'
        ],
        'dogs':[
            '/static/images/dogs/dog1.jpeg',
            '/static/images/dogs/dog2.jpeg',
            '/static/images/dogs/dog3.jpeg',
            '/static/images/dogs/dog4.jpeg',
            '/static/images/dogs/dog5.jpeg',
            '/static/images/dogs/dog6.jpeg',
            '/static/images/dogs/dog7.jpeg',
            '/static/images/dogs/dog8.jpeg',
            '/static/images/dogs/dog9.jpeg',
            '/static/images/dogs/dog10.jpeg'
        ]
    }

def test(request):
    return render(request,"views/insert.html",{
        'data':data,
    })
    
    
def app(request):
    images_grouped_by_type = Image.objects.all().order_by('type')
    # Loop through grouped images and filter by type
    images_by_type = {}
    for image in images_grouped_by_type:
        if image.type not in images_by_type:
            images_by_type[image.type] = []
        images_by_type[image.type].append(image)
        
    print(images_by_type)
    if request.method == "POST":
        cats = request.FILES.getlist('cats')
        dogs = request.FILES.getlist('dogs')
        
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

        

    # data = Image.objects.all()  # Fetch all images to display
    return render(request, "views/test.html", {'data': images_by_type})