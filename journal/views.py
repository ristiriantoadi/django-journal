from django.http import HttpResponse
from django.shortcuts import render
from journal.models import Entri
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect

def index(request):
    # return HttpResponse("Hello, world. You're at the journal index.")
    # e = Entri(title="entri 1",content="lorem ipsum dolor sit amet",author=1)
    # e.save()
    if request.user.is_authenticated:
        return HttpResponse(request.user.username)
    return render(request, 'journal/index.html')
def post(request):
    all_entries = Entri.objects.get(kolom="someValue")
    print(all_entries)
    return HttpResponse(all_entries)

def add_post(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        content = request.POST.get('content','')
        author = request.POST.get('author','')

        e = Entri(title=title,content=content,author=author)
        e.save()

        entries = Entri.objects.all()

        return HttpResponse(entries)

    return render(request, 'journal/add_post.html')

def login_user(request):
    if request.method == "POST":
        # return HttpResponse("a POST request")
        username = request.POST.get('username', '')
        # email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        # return HttpResponse("register successful")
        if user is not None:
            login(request, user)
            # return redirect('/journal')
            return HttpResponse(user.username)
    return render(request, 'journal/login.html')

def register(request):
    if request.method == "POST":
        # return HttpResponse("a POST request")
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = User.objects.create_user(username, email, password)
        return HttpResponse("register successful")
    return render(request, 'journal/register.html')