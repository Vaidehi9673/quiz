from django.shortcuts import render, redirect
from django.http import HttpResponse
from myquiz.models import Contact, Question
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.
def home(request):
    allposts = Question.objects.all()
    #print(allposts)
    context = {
        'allposts':allposts
    }
    return render(request, "myquiz/home.html",context)
def about(request):
    return render(request, 'myquiz/about.html')

def contact(request):
    if request.method == "POST":
        email=request.POST['email']
        uname=request.POST['uname']
        text=request.POST['text']
        #print(email, uname, text)
        con = Contact(email=email, uname=uname, text=text)
        con.save()
        messages.success(request, 'Message has been sent succesfully!')
    return render(request, 'myquiz/contact.html')

def signup(request):
    if request.method == "POST":
        email=request.POST['email']
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        pwd2=request.POST['pwd2']
        #checking validations
        print(email, uname, pwd, pwd2)
        if(len(uname)>3 and len(email)>3 and pwd==pwd2):
            user = User.objects.create_user(uname, email, pwd)
            user.save()
            messages.success(request, 'Registered successfully')
            return redirect("/")
        else:
            messages.error(request, 'Please try again')
            return redirect("/")

def authlogin(request):
    if request.method=="POST":
        loginuser=request.POST['loginuser']
        loginpass=request.POST['loginpass']
        user = authenticate(username=loginuser, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect("/")
        else:
            messages.error(request, 'Please try to login again')
            return redirect("/")

def authlogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect("/")

def quizpage(request):
    if request.method=="POST":
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total=total+1
            print(request.POST.get(q.Ques))
            print(q.ans)
            print()
            if q.ans==request.POST.get(q.Ques):
                score+=1
                correct+=1
            else:
                wrong+=1
        percent=(score/(total*10))*100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        messages.success(request, 'You have successfully completed the quiz!')
        return render(request,"myquiz/result.html", context)