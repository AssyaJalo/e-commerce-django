from django.urls import path
from .views import accueil, contact, delete_article, detailsArticle, edit_article, navbar, new_article, propos,  useradmin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', accueil, name='accueil'),
    path('user_admin/' , useradmin, name= 'useradmin'),
    path('new_article/' , new_article, name= 'new_article'),
    path('navbar/' , navbar, name= 'navbar'),
    path('new_article/<int:id>/', detailsArticle,name='detailsArticle'),
    path('edit_article/<int:id>/', edit_article,name='edit_article'),
    path('delete_article/<int:id>/', delete_article,name='delete_article'),
    path('contact/', contact, name='contact'),
    path('propos/', propos, name='propos'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)