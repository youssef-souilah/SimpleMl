from django.shortcuts import render
from django.http import HttpResponse

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
        'data':data
    })
    
def app(request):
    
    return render(request,"views/test.html",{
        'data':data
    })