from django.http import HttpResponse
from django.shortcuts import render
from journal.models import Entri,Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect

def index(request):
    # return HttpResponse("Hello, world. You're at the journal index.")
    # e = Entri(title="entri 1",content="lorem ipsum dolor sit amet",author=1)
    # e.save()

    posts=[
        {
            'title':'entri 1',
            'author':'adi3d',
        },
                {
            'title':'entri 2',
            'author':'adi3d',
        },
        {
            'title':'entri 3',
            'author':'adi3d',
        }
    ]
    context={
        # 'posts': Entri.objects.all()
        'posts': Post.objects.filter(user=User.objects.get(username=request.user.username))
    }

    if request.user.is_authenticated:
        return render(request, 'journal/index.html',context)
    # return render(request, 'journal/index.html',context)
    return redirect('login')
def post(request):
    all_entries = Entri.objects.get(kolom="someValue")
    print(all_entries)
    return HttpResponse(all_entries)

def add_post(request):
    # entri = Entri.objects.get(pk = 2) 
    # entri.delete()
    if request.method == "POST":
        title = request.POST.get('title', '')
        content = request.POST.get('content','')
        user=User.objects.get(username=request.user.username)
        e = Post(title=title,content=content,user=user)
        e.save()

        posts = Post.objects.all()

        return redirect('/journal')

    # title = "Something Wicked This Way Come"
    # content = "this is a post"
    # user=User.objects.get(username=request.user.username)
    # e = Post(title=title,content=content,user=user)
    # e.save()
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
            return redirect('journal/')
    return render(request, 'journal/login.html')

def logout_user(request):
    logout(request)
    return HttpResponse("logout success")

def register(request):
    if request.method == "POST":
        # return HttpResponse("a POST request")
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = User.objects.create_user(username, email, password)
    return render(request, 'journal/register.html')