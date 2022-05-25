from django.urls import path,include

from ESapp.views import PublisherDocumentView, index

urlpatterns =[
path('search/' , PublisherDocumentView.as_view({'get': 'list'})),
path('' , index),
]

