from django.conf.urls import url
from . import rest_views

urlpatterns = (
    url(r'^user-details/$', rest_views.UserDetailsView.as_view(), name='user_details_view'),

)