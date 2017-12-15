# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Person
# Create your views here.
def home(request):
	return render(request, 'home.html')

def get_name(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    persons = Person.objects.filter(name__icontains=q)
    results = []
    for pr in persons:
      person_json = {}
      person_json = pr.name
      results.append(person_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)