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
    path('edit_topic/<topic_id>', views.edit_topic, name='edit_topic'),
    path('edit_publication/<publication_id>',
         views.edit_publication, name='edit_publication'),
    path('delete_topic/<topic_id>', views.delete_topic, name='delete_topic'),
    path('delete_publication/<publication_id>',
         views.delete_publication, name='delete_publication'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
