import requests
import json
from django.http import JsonResponse
import os

giphy_key = os.environ.get("GIPHY_KEY")


def pokemon(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]
    types = []
    for type in body['types']:
        types.append(type['type']['name'])
    giphy_response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={name}&limit=1")
    giphy_body = json.loads(giphy_response.content)
    gif_url = giphy_body['data'][0]['url']
    # print(f"The location of the gif is: {gif_url}")
    return JsonResponse({'id': id, 'response': name, 'types': types, 'gif': gif_url})
