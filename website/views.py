from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from website.models import Contact
#from website.forms import NameForm , ContactForm , NewsletterForm
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'website/home-one.html')

