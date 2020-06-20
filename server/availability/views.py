import ast
import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from availability.models import POI, Availability, Features


def list_POIs(request):
    return JsonResponse({
        'data': [t.to_dict() for t in POI.objects.all().order_by('-updated_at')],
    })


def get_availability(request, pk):
    return JsonResponse({
        'data': [availability.to_dict() for availability in Availability.objects.filter(poi=pk)],
    })


def get_feature(request, pk):
    return JsonResponse({
        'data': [feature.to_dict() for feature in Features.objects.get(poi=pk)],
    })


@csrf_exempt
@require_POST
def create_POI(request):

    data = json.loads(request.body)
    poi = data.get('poi')
    space = data.get('space')
    did = data.get('did')
    title = data.get('title')
    description = data.get('description')
    precision = data.get('precision')

    new_poi = POI(did=did, poi=poi, space=space, title=title, description=description,
                                precision=precision)
    new_poi.save()

    return JsonResponse(new_poi.to_dict(), status=201)


@csrf_exempt
def create_availability(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        poi = data.get('poi')
        space = data.get('space')
        did = data.get('did')
        status = data.get('status')
        schedule = data.get('schedule')
        challenge = data.get('challenge')
        info = data.get('info')
        availability = Availability(did=did, poi_id=poi, space=space, schedule=schedule,
                                    challenge=challenge, info=info)
        availability.save()

        return JsonResponse(availability.to_dict(), status=201)

    return JsonResponse({}, status=200)


@csrf_exempt
@require_POST
def create_feature(request):
    data = json.loads(request.body)
    poi = data.get('poi')
    space = data.get('space')
    did = data.get('did')
    status = data.get('status')
    info = data.get('info')
    challenge = data.get('challenge')

    feature = Features(did=did, poi=poi, space=space, status=status, info=info,
                       challenge=challenge)
    feature.save()

    return JsonResponse(feature.to_dict(), status=201)
