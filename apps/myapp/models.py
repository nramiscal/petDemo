from django.db import models

# Create your models here.

class PetManager(models.Manager):
    def pet_validator(self, form):
        print("3. inside pet validator method in models")
        print("4. printing form: (i.e. request.POST)")
        print(form) # i.e. print the request.POST
        print("5. starting validations")
        errors = {}

        name = form['name']
        breed = form['breed']
        species = form['species']
        age = form['age']

        if not name:
            errors['name'] = "Name cannot be blank"
        elif len(name) < 2:
            errors['name'] = "Name must be at least 2 characters"

        if not species:
            errors['species'] = "Species cannot be blank"

        if not age:
            errors['age'] = "Age cannot be blank"

        print("6. finished validations")
        print("7. returning errors dictionary to process method in views")
        return errors


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # pets --> Pet table

    def __repr__(self):
        return f"<User {self.fname} {self.lname} id: {self.id}>"

class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, default=None)
    species = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name="pets", on_delete=models.CASCADE)

    objects = PetManager()

    def __repr__(self):
        return f"<Pet {self.name} {self.species} id: {self.id}>"
