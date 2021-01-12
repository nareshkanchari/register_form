from django.shortcuts import render
from .models import UREG


# Create your views here.

def home(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        print(firstname,lastname,address,phonenumber,city,zip)
        data = UREG(
            firstname=firstname,
            lastname=lastname,
            address=address,
            phonenumber=phonenumber,
            city=city,
            zip=zip,
        )
        data.save()
        print("**"*10)
        print(UREG.objects.all())

        message = 'data inserted successfully'
        return render(request,'home.html',{"message": message})

    return render(request, 'home.html')
