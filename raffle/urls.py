from django.urls import path

from raffle import views

urlpatterns = [
    path('events/upcoming/', views.EventView.as_view()),
    path('events/', views.EventCreateView.as_view()),
    path('events/<int:event_id>/participate/', views.Participate.as_view()),
    path('winners/', views.WinnerView.as_view()),
]
