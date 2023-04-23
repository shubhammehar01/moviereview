from django.contrib import admin
from .models import User
from .models import Movie
from .models import Review
from .models import Contact
# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Movie)
admin.site.register(Review)
