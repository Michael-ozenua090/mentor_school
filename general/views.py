from django.shortcuts import redirect, render
from django.urls import reverse

from general.forms import ContactForm

# Create your views here.
def homepage(request):
    context = {
       'title' : 'Mentor - Homepage',
       'class' : 'active'
    }
    return render(request, 'general/index.html', context)

def about(request):
    context = {
       'title' : 'Mentor - About',
       'sub_title' : 'About',
       'class' : 'active'

       
    }
    return render(request, 'general/about.html', context)

def contact(request):
    contact = ContactForm(request.POST or None )
    context = {
       'title' : 'Mentor - Contact',
       'sub_title' : 'Contact',
       'form' : contact,
       'class' : 'active'

    }
    if request.POST:
        if contact.is_valid():
            contact.save()
            return redirect(reverse('contact'))
    return render(request, 'general/contact.html', context)

def course_details(request):
    context = {
        'title' : 'Mentor - Course Details',
       'sub_title' : 'Course Details',
       'class' : 'active'

    }
    return render(request, 'general/course-details.html', context)

def course(request):
    context = {
        'title' : 'Mentor - Course',
       'sub_title' : 'Course'
    }
    return render(request, 'general/courses.html', context)

def events(request):
    context={
        'title' : 'Mentor - Events',
       'sub_title' : 'Events',
       'class' : 'active'

    }
    return render(request, 'general/events.html', context)

def pricing(request):
    context = {
        'title' : 'Mentor - Pricing',
       'sub_title' : 'Pricing',
       'class' : 'active'

    }
    return render(request, 'general/pricing.html', context)

def lecturers(request):
    context ={
        'title' : 'Mentor - Lecturers',
       'sub_title' : 'Lecturers',
       'class' : 'active'

    }
    return render(request, 'general/trainers.html', context)


