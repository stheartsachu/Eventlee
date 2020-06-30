from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from ApplicationUsers.form import ApplicationuserForm
# Create your views here.
from ApplicationUsers.models import users
def home(request):
    return render(request,"index.html")
def Contact(request):
    return render(request,"contact.html")
def gallery(request):
    return render(request,"gallery.html")
def signup(request):
    if request.method == 'POST':
        form = ApplicationuserForm(request.POST)
        f = form.save(commit=False)
        f.first_name = request.POST['fn']
        f.last_name = request.POST['ln']
        f.email = request.POST['email']
        if request.POST['p1'] == request.POST['p2']:
            f.password = request.POST['p2']
        else:
            return HttpResponse("<h1> Password and Confirm password is not same</h1>")
        f.status = True
        f.save()
        return HttpResponse("User is created sucessfully now, can login to website")
    return render(request, 'registration.html')

def login(request):
    if request.method == "POST":
        un = request.POST["email"]
        up = request.POST["password"]
        try:
            data = users.objects.get(email=un)

        except:
            return render(request, "login.html", {'emailerror': True})

        dp = data.password
        active = data.status

        if (active == False):
            return render(request, "login.html", {'activeerror': True})

        else:
            if (dp == up):
                request.session['emailid'] = un
                request.session['Authentication'] = True
                return HttpResponse("You are sucessfullly login")
            else:
                return render(request, "login.html", {'passworderror': True})
    return render(request, "login.html")