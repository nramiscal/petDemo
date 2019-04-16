from django.db import models

# Create your models here.

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
    breed = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name="pets", on_delete=models.CASCADE)

    def __repr__(self):
        return f"<Pet {self.name} {self.species} id: {self.id}>"
