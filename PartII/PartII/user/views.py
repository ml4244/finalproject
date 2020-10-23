from django.shortcuts import render
from django.shortcuts import redirect
from user.models import Squirrel
from django.shortcuts import HttpResponse
from django.http import JsonResponse,HttpResponseRedirect
import json
from django.core.serializers import serialize
from django.core import serializers


def to_sightings_all(request):
    return render(request, 'sightings_all.html')

def to_sightings_single(request, id):
    unique_squirrel_id_testvalue = Squirrel.objects.get(unique_squirrel_id=id)
    print(id)
    return render(request, 'sightings_single.html', {"obj": unique_squirrel_id_testvalue})

def query_single_sightings_data(request, bid):
    print(bid)
    # unique_squirrel_id_testvalue = serializers.serialize("json", Squirrel.objects.get(unique_squirrel_id=bid))
    unique_squirrel_id_testvalue = Squirrel.objects.get(unique_squirrel_id=bid)
    print(unique_squirrel_id_testvalue)
    # print(id)
    return HttpResponse(unique_squirrel_id_testvalue)

def sightings_add(request):
    unique_squirrel_id = request.POST.get("unique_squirrel_id")
    x = request.POST.get("x")
    y = request.POST.get("y")
    shift = request.POST.get("shift")
    date = request.POST.get("date")
    age = request.POST.get("age")
    primary_fur_color = request.POST.get("primary_fur_color")
    location = request.POST.get("location")
    specific_location = request.POST.get("specific_location")
    running = request.POST.get("running")
    chasing = request.POST.get("chasing")
    climbing = request.POST.get("climbing")
    eating = request.POST.get("eating")
    foraging = request.POST.get("foraging")
    other_activities = request.POST.get("other_activities")
    kuks = request.POST.get("kuks")
    quaas = request.POST.get("quaas")
    moans = request.POST.get("moans")
    tail_flags = request.POST.get("tail_flags")
    tail_twitches = request.POST.get("tail_twitches")
    approaches = request.POST.get("approaches")
    indifferent = request.POST.get("indifferent")
    runs_from = request.POST.get("runs_from")
    Squirrel.objects.create(unique_squirrel_id=unique_squirrel_id, x=x, y=y,
                            shift=shift, date=date, age=age,
                            primary_fur_color=primary_fur_color, location=location, specific_location=specific_location,
                            running=running, chasing=chasing, climbing=climbing,
                            eating=eating, foraging=foraging, other_activities=other_activities,
                            kuks=kuks, quaas=quaas, moans=moans,
                            tail_flags=tail_flags, tail_twitches=tail_twitches, approaches=approaches,
                            indifferent=indifferent, runs_from=runs_from)
    return render(request, 'sightings.html')

def query_data(request):
    ajax_testvalue = serializers.serialize("json", Squirrel.objects.all())
    return HttpResponse(ajax_testvalue)

def query_all_points(request):
    ajax_points = serializers.serialize("json", Squirrel.objects.all())
    return HttpResponse(ajax_points)


