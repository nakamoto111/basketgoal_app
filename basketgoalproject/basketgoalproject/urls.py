from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import indexfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manageuser/', include('manageuser.urls')),
    path('managegoal/', include('managegoal.urls')),
    path('manageplace/', include('manageplace.urls')),
    # index.htmlに移る(indexfuncでログイン前、ログイン後画面に遷移する)
    path('index/',indexfunc, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


