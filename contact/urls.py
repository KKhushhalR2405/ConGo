from django.urls import re_path, include
from . import views

app_name = 'contact'

urlpatterns = [
        
        re_path(r"display/$", views.UserAllContacts.as_view(),
                name="displaycontacts"),
        re_path(r"^details/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
                views.ContactDetails.as_view(), name="contactdetails"),
        re_path(r"create/$", views.CreateContact.as_view(), name="create"),
        re_path(r"^update/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
                views.UpdateContact.as_view(), name="update"),
        re_path(r"^delete/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
            views.DeleteContact.as_view(), name="delete"),


]
