from django.shortcuts import render,HttpResponse
from ApplicationAdmin.form import ApplicationAdminForm

# Create your views here.
def eventregister(request):
    if request.method == 'POST':
        form = ApplicationAdminForm(request.POST)
        f = form.save(commit=False)
        f.eventname = request.POST['eventname']
        f.eventcategory= request.POST['eventcategory']
        f.eventdescription = request.POST['eventdescription']
        f.eventdate = request.POST['eventdate']
        f.eventtime = request.POST['eventtime']
        f.eventlocation= request.POST['eventlocation']
        f.save()
        return HttpResponse("Event is created sucessfully")
    return render(request, 'AdminEventRegister.html')