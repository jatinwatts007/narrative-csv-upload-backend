from django.urls import path
from UploadAPP.views import UploadCSVFile

urlpatterns = [
    path('csv/', UploadCSVFile.as_view()),
]

# we are using here because django runs two processes but urls is read in only one of them starting scheduler.
