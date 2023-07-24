"""GodsOwnResort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ResortApp import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CommonHome,name='CommonHome'),
    path('CustomerSignUp/',views.CustomerSignUp,name='CustomerSignUp'),
    path('ResortSignUp/',views.ResortSignUp,name='ResortSignUp'),
    path('SignIn/',views.SignIn,name='Sign In'),
    
    
    
    
    path('AdminHome/',views.AdminHome,name='Admin Home'),
    path('AdminAddCategory/',views.AdminAddCategory,name='Admin Add Category'), 
    path('AdminViewCustomers/',views.Admin_View_Customers,name='Admin View Customers'),
    path('AdminViewResorts/',views.AdminViewResorts,name='AdminViewResorts'),
    path('AdminViewFeedback/',views.AdminViewFeedback,name='Admin View Feedback'),
    path('AdminViewApprovedResorts/',views.AdminViewApprovedResorts,name='AdminViewApprovedResorts'),
    
    
    
    
    path('CustomerHome/',views.CustomerHome,name='Customer Home'),
    path('CustomerSearchResorts/',views.CustomerSearchResorts,name='CustomerSearchResorts'),
    path('CustomerViewResortHome/',views.CustomerViewResortHome,name='CustomerViewResortHome'),
    path('CustomerViewResortAccommodation/',views.CustomerViewResortAccommodation,name='CustomerViewResortAccommodation'),
    path('CustomerViewResortAccoDetails/',views.CustomerViewResortAccoDetails,name='CustomerViewResortAccoDetails'),
    path('CustomerBookResortAccommodation/',views.CustomerBookResortAccommodation,name='CustomerBookResortAccommodation'),
    path('CustomerViewResortDining/',views.CustomerViewResortDining,name='CustomerViewResortDining'),
    path('CustomerViewResortDiningDetails/',views.CustomerViewResortDiningDetails,name='CustomerViewResortDiningDetails'),
    path('CustomerBookResortDining/',views.CustomerBookResortDining,name='CustomerBookResortDining'),
    path('CustomerViewResortAyurvedha/',views.CustomerViewResortAyurvedha,name='CustomerViewResortAyurvedha'),
    path('CustomerViewResortAyurDetails/',views.CustomerViewResortAyurDetails,name='CustomerViewResortAyurDetails'),
    path('CustomerBookResortAyurvedha/',views.CustomerBookResortAyurvedha,name='CustomerBookResortAyurvedha'),
    path('CustomerViewResortPackage/',views.CustomerViewResortPackage,name='CustomerViewResortPackage'),
    path('CustomerViewResortPackageDetails/',views.CustomerViewResortPackageDetails,name='CustomerViewResortPackageDetails'),
    path('CustomerBookResortPackage/',views.CustomerBookResortPackage,name='CustomerBookResortPackage'),
    path('CustomerViewResortEvents/',views.CustomerViewResortEvents,name='CustomerViewResortEvents'),
    path('CustomerViewResortEventsDetails/',views.CustomerViewResortEventsDetails,name='CustomerViewResortEventsDetails'),
    path('CustomerBookResortEvents/',views.CustomerBookResortEvents,name='CustomerBookResortEvents'),
    path('CustomerViewResortFacilities/',views.CustomerViewResortFacilities,name='CustomerViewResortFacilities'),
    path('CustomerViewPaymentNotification/',views.CustomerViewPaymentNotification,name='CustomerViewPaymentNotification'),
    path('CustomerViewAccoPayment/',views.CustomerViewAccoPayment,name='CustomerViewAccoPayment'),
    path('CustomerViewDiningPayment/',views.CustomerViewDiningPayment,name='CustomerViewDiningPayment'),
    path('CustomerViewEventPayment/',views.CustomerViewEventPayment,name='CustomerViewEventPayment'),
    path('CustomerViewPackagePayment/',views.CustomerViewPackagePayment,name='CustomerViewPackagePayment'),
    path('CustomerViewAyurPayment/',views.CustomerViewAyurPayment,name='CustomerViewAyurPayment'),
    path('CustomerAddFeedback/',views.CustomerAddFeedback,name='CustomerAddFeedback'),
    path('payment1/',views.payment1,name='payment1'),
    path('payment2/',views.payment2,name='payment2'),
    path('payment3/',views.payment3,name='payment3'),
    path('payment4/',views.payment4,name='payment4'),
    path('payment5/',views.payment5,name='payment5'),
    
    
    
    
    path('ResortHome/',views.ResortHome,name='ResortHome'),
    path('ResortAddAccommodation/',views.ResortAddAccommodation,name='ResortAddAccommodation'),
    path('ResortAddDining/',views.ResortAddDining,name='ResortAddDining'),
    path('ResortAddHalls/',views.ResortAddHalls,name='ResortAddHalls'),
    path('ResortAddHomepage/',views.ResortAddHomepage,name='ResortAddHomepage'),
    path('ResortAddFacilities/',views.ResortAddFacilities,name='ResortAddFacilities'),
    path('ResortAddPackage/',views.ResortAddPackage,name='ResortAddPackage'),
    path('ResortAddAyurvedha/',views.ResortAddAyurvedha,name='ResortAddAyurvedha'),
    path('ResortViewAccoBooking/',views.ResortViewAccoBooking,name='ResortViewAccoBooking'),
    path('ResortViewDiningBooking/',views.ResortViewDiningBooking,name='ResortViewDiningBooking'),
    path('ResortViewEventBooking/',views.ResortViewEventBooking,name='ResortViewEventBooking'),
    path('ResortViewPackageBooking/',views.ResortViewPackageBooking,name='ResortViewPackageBooking'),
    path('ResortViewAyurBooking/',views.ResortViewAyurBooking,name='ResortViewAyurBooking'),



#updated urls
    path('rcv/',views.resortviewaccomadation,name='resortviewaccomadation'),
    path('rvaupdate/',views.rvaupdate,name='rvaupdate'),
    path('rvdupdate/',views.rvdupdate,name='rvaupdate'),
    path('resortviewdining/',views.resortviewdining,name='resortviewdining'),
    path('rvayurupdate/',views.rvayurupdate,name='rvayurupdate'),
    path('resortviewayur/',views.resortviewayur,name='resortviewayur'),
    path('resortviewhall/',views.resortviewhall,name='resortviewhall'),
    path('rvhallupdate/',views.rvhallupdate,name='rvhallupdate'),
    path('rvpackageupdate/',views.rvpackageupdate,name='rvpackageupdate'),

    path('resortviewpackage/',views.resortviewpackage,name='resortviewpackage'),





    



    

]
