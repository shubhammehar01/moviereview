from django.shortcuts import render,HttpResponse,redirect
from .models import User,Contact
from django.contrib import messages
from .models import Movie
import requests
import pandas as pd
# Create your views here.
def index(request):
    movie = Movie.getDetails()[:1000:10]
    email = request.session.get('email')
    return render(request,'index.html',{'email':email,'movie':movie})
def navbar(request):
    email = request.session.get('email')
    return render(request,'navbar.html',{'email':email})
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.verifyemail(email)
        if user:
            flag = User.get_pass(email,password)
            if flag:
                messages.success(request, 'Login successfully !! ')
                request.session['email'] = email
                data = User.verifyemail(email)
                if data:  
                    request.session['first_name'] = data.first_name
                    request.session['last_name'] = data.last_name

                return redirect('index')
            else:
                messages.error(request,'password invalid !!')
                return redirect('login')
        else:
            messages.error(request, 'invalid email !')
            return redirect('login')

    return render(request, 'login.html')
def about(request):
    email = request.session.get('email')
    return render(request, 'about.html',{'email':email})
def signout(request):
    
    try:
        del request.session['email']
    except:
        pass
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')
def contact(request):
    email = request.session.get('email')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        textarea = request.POST.get('textarea')
        data = Contact(name=name, email=email, mobile=mobile, textarea=textarea)
        data.save()
        messages.success(request, 'your form submitted success fully')
    return render(request, 'contact.html',{'email':email})
def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        flag = User.verifyemail(email)

        if flag:
            messages.error(request, "username already exits please try some others")
            return redirect('signup')

        if phone.strip().isdigit()==False:
            messages.error(request, "phone no must be numeric!!")
            return redirect('signup')

        if len(password)<5:
            messages.error(request, "make a strong password!!")
            return redirect('signup')

        myuser = User(first_name=fname,last_name=lname,phone=phone, email=email, password=password)
        myuser.save()
        messages.success(request, "your account created successfully")

        request.session['email'] = email
        data = User.verifyemail(email)
        if data:
            request.session['first_name'] = data.first_name
            request.session['last_name'] = data.last_name

        return redirect('index')
    return render(request, 'signup.html')
def details(request):
    id=0
    if request.method=='POST':
        id = request.POST['takeid']
    data = Movie.getDetailsbyid(id)
    return render(request,'detail.html',{'final':data})

def getimg(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1c28161e325733b2cbc131577612f3ee&language=en-US'.format(id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500'+data['poster_path']
    

def account(request):
    email = request.session.get('email')
    email = request.session.get('email')
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    return render(request, 'account.html', {'email':email, 'first_name':first_name,'last_name':last_name,'email':email})
    '''df = pd.read_csv('myapp/static/mydata.csv')
    for i in range(4655,len(df)):
        id = int(df['id'][i])
        title = df['title'][i]
        img = getimg(id)
        budget = df['budget'][i]
        genre = df['genres'][i]
        language = df['original_language'][i]
        overview = df['overview'][i]
        release = df['release_date'][i]
        revenue = df['revenue'][i]
        duration = df['runtime'][i]
        tagline = df['tagline'][i]
        rating = df['vote_average'][i]
        t_rating = df['vote_count'][i]
        
        print(id,title,img,budget,genre,language,overview,release,revenue,duration,tagline,rating,t_rating)
        data = Movie(id=id,title=title,img=img,budget=budget,genre=genre,language=language,overview=overview,release=release,revenue=revenue,duration=duration,tagline=tagline,rating=rating,t_rating=t_rating)
        data.save()
    return render(request,'account.html')'''


