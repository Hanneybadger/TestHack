from django.conf.urls import url
from testweather import views
urlpatterns = [
	url(r"^$", views.startpage),
]
