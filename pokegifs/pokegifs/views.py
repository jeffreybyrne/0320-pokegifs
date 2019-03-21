import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def pokemon(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]
    types = []
    for type in body['types']:
        types.append(type['type']['name'])
    return JsonResponse({'id': id, 'response': name, 'types': types})
