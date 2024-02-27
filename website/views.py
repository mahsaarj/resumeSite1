from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from website.models import Contact
#from website.forms import NameForm , ContactForm
from django.contrib import messages

from website.forms import ContactForm


# Create your views here.
def index_view(request):
    return render(request, 'website/home-one.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
           messages.add_message(request,messages.SUCCESS,'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket did not submitted')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})
