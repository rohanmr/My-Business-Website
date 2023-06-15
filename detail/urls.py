from enroll import views
from django.urls import path
from detail import views
urlpatterns =[
    path('grocerry/',views.grocerry,name='grocerry'),
    path('steel/',views.steel,name='steel'),
    path('hardware/',views.hardware,name='hardware'),
    path('footwear/',views.footwear,name='footwear'),
    path('fashion/',views.Fashion,name='fashion'),
    path('Jwellery/',views.jewellery,name='jewellery'),
    path('fastfood/',views.fastfood,name='fastfood'),
    path('mobile/',views.Mobile,name='mobile'),
    path('gift/',views.gift,name='gift'),
    path('watch/',views.watch,name='watch'),
    path('electronic/',views.electronic,name='electronic'),   
    path('computer/',views.computer,name='computer'),   
    path('coffee/',views.coffee,name='coffee'),   
    path('pharmacy/',views.pharmacy,name='pharmacy'),   
]
