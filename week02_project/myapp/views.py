from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forms import PersonForm
from models import Person, Image
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

def home(request):
	return render(request, 'home.html', {'key': "value" })

def MyGallery(request):
	images = Image.objects.all().order_by('?')[:12]
	return render(request, 'gallery.html', {'images': images})

def GetSession(request, id=1):
	list_id = request.session.get('key', [])
	list_id.append(id)

	image = Image.objects.get(id=id)
	request.session['key'] = list_id
	for i in Session.objects.all():
		print SessionStore().decode(i.session_data)

	request.session.set_expiry(5)
	return render(request, 'show_session.html',
		{
			'id' :id,
			'image' :image
		})



class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class ListPersonView(ListView):
    model = Person
    template_name='person_list.html'
