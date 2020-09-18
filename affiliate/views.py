from django.shortcuts import render
from .models import Details
from.forms import MemberForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_details = Details.objects.all
    return render(request, 'home.html',{'all':all_details})

def about(request):
    return render(request, 'about.html',{})

def contact(request):

    if request.method =="POST":

        form = MemberForm(request.POST or None)

        if form.is_valid():

            form.save()

        messages.success(request,('Message Sent!'))

        return render(request, 'contact.html',{})

    else:
        return render(request, 'contact.html',{})








