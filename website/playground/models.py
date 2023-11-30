from django.db import models

# Create your models here.

class stringers(models.Model):
    fullName = models.CharField(max_length = 100)
    streetAddress = models.CharField(max_length = 250)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 2) #add picking fields in the future https://docs.djangoproject.com/en/4.2/topics/db/models/#field-types
    postalCode = models.CharField(max_length = 6)
    phoneNumber = models.CharField(max_length = 10)
    emailAddress = models.EmailField()

    class rating(models.IntegerChoices):
        zero= 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
    rating = models.IntegerField(choices = rating.choices)

    cost = models.DecimalField(max_digits=6, decimal_places=2) #max cost = 9999.99
    numberOfLifeTimeCustomers = models.CharField(max_length = 10)
    dateJoined = models.DateTimeField(auto_now_add = True)


    class sport(models.IntegerChoices):
        badminton = 1
        tennis = 2
        squash = 3
    sport = models.IntegerField(choices = sport.choices)

    def __str__(self):
            return self.fullName

class customers(models.Model):
    fullName = models.CharField(max_length = 100)
    streetAddress = models.CharField(max_length = 250)
    city = models.CharField(max_length = 100)
    province = models.CharField(max_length = 2) #add picking fields in the future https://docs.djangoproject.com/en/4.2/topics/db/models/#field-types
    postalCode = models.CharField(max_length = 6)
    phoneNumber = models.CharField(max_length = 10)
    emailAddress = models.EmailField()
    dateOfBirth = models.DateField()

    dateJoined = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.fullName
