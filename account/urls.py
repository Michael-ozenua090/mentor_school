from django.urls import path
from account.views import add_scores, dashboard, loginpage, logoutpage, registration


urlpatterns = [
    path('registration', registration, name='registration-page'),
    path('login', loginpage, name='login-page'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout',logoutpage, name='logout-page' ),
    path('add-score', add_scores, name='add-score')


    
]
