from django.shortcuts import render
from django.shortcuts import redirect
from user.models import Squirrel
from django.shortcuts import HttpResponse
from django.http import JsonResponse,HttpResponseRedirect
import json
from django.core.serializers import serialize
from django.core import serializers

def to_index(request):
    return render(request, 'index.html')

def to_map(request):
    return render(request, 'map.html')

def to_sightings(request):
    return render(request, 'sightings.html')

def to_sightings_stats(request):
    return render(request, 'sightings_stats.html')

def query_data(request):
    ajax_testvalue = serializers.serialize("json", Squirrel.objects.all())
    return HttpResponse(ajax_testvalue)

def query_all_points(request):
    ajax_points = serializers.serialize("json", Squirrel.objects.all())
    return HttpResponse(ajax_points)


