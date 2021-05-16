from django.utils import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]