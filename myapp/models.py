from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    # id = models.IntegerField(primary_key=True,editable=False)
    first_name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=100,default='')

    def __str__(self):
        return str(self.id) +' - '+ self.first_name+' '+self.last_name
    

    @staticmethod
    def verifyemail(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_pass(email,password):
        try:
            return User.objects.get(email=email,password=password)
        except: 
            return False

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    mobile = models.IntegerField()
    textarea = models.CharField(max_length=400)
    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.IntegerField(primary_key=True,editable=False)
    title = models.CharField(max_length=100,default='Not Found')
    img = models.CharField(max_length=1000,default='not fount')
    budget = models.BigIntegerField(default=-1)
    genre = models.CharField(max_length=2000,default='fantasy')
    language = models.CharField(max_length=100,default='en')
    overview = models.CharField(max_length=5000,default='not found')
    release = models.CharField(max_length=20,default='released')
    revenue = models.BigIntegerField(default=-1)
    duration = models.FloatField(default=-1)
    tagline = models.CharField(max_length=200,default='not found')
    rating = models.FloatField(default=5)
    t_rating = models.IntegerField(default=1000)

    def __str__(self):
        return str(self.id)+' - ' +self.title
    @staticmethod
    def getDetails():
        return Movie.objects.all()
    @staticmethod
    def getDetailsbyid(id=''):
        return Movie.objects.get(id=id)
    @staticmethod
    def delete_everything():
        Movie.objects.all().delete()

class Review(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    movieid = models.ForeignKey(Movie,on_delete=models.CASCADE)
    review = models.CharField(max_length=5000)