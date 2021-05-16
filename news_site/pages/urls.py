from django.urls import path
from .views import homePageView, NewsPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('testing', NewsPageView.as_view(), name='testing'),
]