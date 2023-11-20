from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PublicationForm
from .forms import TopicForm
from .models import Publication
from .models import Topic


def index(request):
    """ Renderiza a tela inicial """

    topics = Topic.objects.order_by('title')
    context = {'topics': topics}

    return render(request, 'RIEVS/index.html', context)


def topic(request, topic_id):
    """Exibe o tópico e suas respectivas publicações"""

    topic = Topic.objects.get(id=topic_id)
    publications = topic.publication_set.order_by('data_added')

    context = {'topic': topic,
               'publications': publications}

    return render(request, 'RIEVS/topic.html', context)


def publication(request, publication_id):
    """ Exibe os dados de uma publicação baseado no id """

    publication = Publication.objects.get(id=publication_id)
    context = {
        "publication": publication
    }

    return render(request, 'RIEVS/publication.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()

    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('index'))

    context = {'form': form}

    return render(request, 'RIEVS/new_topic.html', context)


@login_required
def new_publication(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = PublicationForm()

    else:
        form = PublicationForm(data=request.POST, files=request.FILES)
        if form.is_valid():

            publication = form.save(commit=False)
            publication.topic = topic

            publication.save()

            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic,
               'form': form}
    return render(request, 'RIEVS/new_publication.html', context)
