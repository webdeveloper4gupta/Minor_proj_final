
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('brain/',views.brain,name="brain_mri"),
  
   path('diab/',views.diab,name='diab')
   ,path('heart/',views.heart,name="heart"),
   path('kid/',views.kidney,name="kidney"),
   path('park/',views.parkinson,name="parkinson"),
   path('aboutus/',views.aboutus,name="aboutus"),
   path('sign',views.sign,name='sign'),
   path('login',views.logins,name="logins"),
   path('logout',views.signout,name="signout"),
   path('enquire',views.enquire,name="enquire")
   ]