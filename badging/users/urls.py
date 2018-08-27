from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:person_id>/', views.detail, name='detail'),
	path('<int:person_id>/badge/', views.badge, name='badge'),
	path('<int:person_id>/add_badge/', views.add_badge, name='add_badge'),
	path('add_person', views.add_person, name='add_person'),
]