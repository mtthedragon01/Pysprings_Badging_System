from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Person, Badge

# Create your views here.
def index(request):
	latest_person_list = Person.objects.order_by('-name')
	#template = loader.get_template('users/index.html')
	context = { 'latest_person_list' : latest_person_list, }
	return render(request, 'users/index.html', context)
	#return HttpResponse(template.render(context, request))

def detail(request, person_id):
	#try:
	#	person = Person.objects.get(pk = person_id)
	#except Person.DoesNotExist:
	#	raise Http404("Person is not in the system.")
	person = get_object_or_404(Person, pk = person_id)
	return render(request, 'users/detail.html', {'person': person})
	
def badge(request, person_id):
	person = get_object_or_404(Person, pk = person_id)
	return render(request, 'users/badge.html', {'person': person})
	
def add_person(request):
	p = Person(name = request.POST['name'])
	if len(p.name) == 0:
		latest_person_list = Person.objects.order_by('-name')
		context = { 'latest_person_list' : latest_person_list, 'error_message' : "Invalid Person Name"}		
		return render(request, 'users/index.html', context )
	else:
		latest_person_list = Person.objects.order_by('-name')
		for person in latest_person_list:
			if p.name == person.name:
				context = { 'latest_person_list' : latest_person_list, 'error_message' : "Person already exists"}
				return render(request, 'users/index.html', context)
		p.save()
		latest_person_list = Person.objects.order_by('-name')
		context = { 'latest_person_list' : latest_person_list, }
		return render(request, 'users/index.html', context)
	
def add_badge(request, person_id):
	person = get_object_or_404(Person, pk = person_id)
	#Tries and excepts must be changed so no blank badges can be entered
	b = Badge(name = request.POST['name'], presenter = request.POST['presenter'])
	if len(b.name) == 0:
		return render(request, 'users/badge.html', {
			'person': person,
			'error_message': "Invalid Badge Name.",
		})
	elif len(b.presenter) == 0:
		return render(request, 'users/badge.html', {
			'person': person,
			'error_message': "Invalid Presenter Name.",
		})
	else:
		badge_list = person.badge_set.order_by('-name')
		for badge in badge_list:
			badge_name = badge.name
			if b.name == badge_name:
				return render(request, 'users/badge.html', {
				'person': person,
				'error_message': "Badge already exists.",
				})
		person.badge_set.create(name = b.name, presenter = b.presenter)
		#print(request.POST)
		return render(request, 'users/detail.html', {'person' : person})