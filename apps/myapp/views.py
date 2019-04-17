from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    # CREATING A USER OR PET
    # user = User.objects.create(fname="Leo", lname="Z", email="leo@gmail.com", phone="567-3456")
    # pet = Pet.objects.create(name="Bubbles", breed="Husky", species="dog", age=5, owner_id=user.id)

    # UPDATING A USER'S FIRST NAME
    # user3 = User.objects.get(id=3)
    # user3.fname = "RJ"
    # user3.save()

    # GETTING ALL THE USERS AND ALL THE PETS
    # users = User.objects.all()
    pets = Pet.objects.all()

    # GET ALL THE PETS OF ONE USER
    # petsOfUser1 = User.objects.get(id=2).pets.all()

    # GET THE OWNER OF ONE PET
    owner = Pet.objects.get(id=4).owner

    context = {
    "num": 5,
    "color": "red",
    # "user": user,
    # "pet": pet,
    # "users": users,
    # "pets": pets,
    # "petsOfUser1": petsOfUser1,
    "owner": owner
    }

    return render(request, 'index.html', context)


def process(request):
    print("1. inside process method in views. received inputs from form through request.POST")
    print("2. passing request.POST to pet_validator to be analyzed")
    errors = Pet.objects.pet_validator(request.POST)
    print("8. back inside process method in views")
    print("9. received errors dictionary from pet_validator")
    print("10. printing errors dictionary:")
    print(errors)

    if not errors:
        # store pet in database
        # redirect to success page

        return redirect ("/success")
    else:
        # transfer error messages to Django messages to display on screen
        # redirect back to form
        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/")


def success(request):
    return render(request, "success.html")
