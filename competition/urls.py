from django.urls import path

from . import views
# view for form to edit an existing Ligue


app_name = 'competition'
urlpatterns = [
    #  /competition/
    path('', views.index, name='index'),
    path('form_ligue/', views.form_ligue, name='form_ligue'),
    path('form_equipe/', views.form_equipe, name='form_equipe'),
    path('form_match/', views.form_match, name='form_match'),
    path('tligue/', views.table_ligue, name='table_ligue'),
    path('tmatch/', views.table_match, name='table_match'),
    path('tequipe/', views.table_equipe, name='table_equipe'),
    path('edit_ligue/<int:ligue_id>/', views.edit_ligue, name='edit_ligue'),
    
]