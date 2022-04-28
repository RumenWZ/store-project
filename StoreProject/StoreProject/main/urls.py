from django.urls import path

from StoreProject.main.views import HomeView, ItemDetailsView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('details/', ItemDetailsView.as_view(), name='details'),
)