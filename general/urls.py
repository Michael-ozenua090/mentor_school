from django.urls import path
from general.views import about, contact, course, course_details, events, homepage, lecturers, pricing

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about', about, name='about_us'),
    path('contact', contact, name='contact'),
    path('courses/details', course_details, name='course-details'),
    path('courses', course, name='courses'),
    path('events', events, name='events'),
    path('pricing', pricing, name='pricing'),
    path('lecturers', lecturers, name='trainers')

    
]
