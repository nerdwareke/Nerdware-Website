from django.urls import path

from .views import (
    home,
    contact_project,
    contact_position,
    contact_say,
    cloudkids,
    aboutus,
    contactus,
    portfolio,
    services,
    cloudkids,
    download_file,
)
app_name = "webpage"
urlpatterns = [
    path("", view=home, name="home"),
    path("contact_project/", view=contact_project, name="contact_project"),
    path("contact_position/", view=contact_position, name="contact_position"),
    path("contact_say/", view=contact_say, name="contact_say"),
    path("cloudkids", view=cloudkids, name="cloudkids"),
    path('download/', view=download_file, name="download"),
    path("aboutus/", view=aboutus, name="aboutus"),
    path("contactus/", view=contactus, name="contactus"),
    path("portfolio/", view=portfolio, name="portfolio"),
    path("services/", view=services, name="services"),
    path("cloudkids/", view=cloudkids, name="cloudkids"),
]