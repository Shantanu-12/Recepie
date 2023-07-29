from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name': 'shantanu' ,'age':20},
        {'name': 'shanu', 'age': 21},
         {'name': 'shivam' ,'age':20},
        {'name': 'shubhra', 'age': 21},
    ]
    
    city=[
         { 'name': 'Shoehar'},
         { 'name':'Muz'},
         {'name':'Patna'},
         { 'name':'Sitamarhi'}
     ]

    return render(request,"index.html",context={'peoples':peoples ,'city':city})

def success_page(request):
    return HttpResponse("Hey this is a success page")
