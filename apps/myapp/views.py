from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # CREATING A USER OR PET
    # user = User.objects.create(fname="Leo", lname="Z", email="leo@gmail.com", phone="567-3456")
    # pet = Pet.objects.create(name="Bubbles", breed="Husky", species="dog", age=5, owner_id=user.id)

    # UPDATING A USER'S FIRST NAME
    user3 = User.objects.get(id=3)
    user3.fname = "RJ"
    user3.save()

    # GETTING ALL THE USERS AND ALL THE PETS
    users = User.objects.all()
    pets = Pet.objects.all()


    context = {
        "num": 5,
        "color": "red",
        # "user": user,
        # "pet": pet,
        "users": users,
        "pets": pets
    }

    return render(request, 'index.html', context)
