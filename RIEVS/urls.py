from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<topic_id>', views.topic, name='topic'),
    path('publication/<publication_id>', views.publication, name='publication'),
    path('new_topic', views.new_topic, name="new_topic"),
    path('new_publication/<topic_id>',
         views.new_publication, name="new_publication"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
