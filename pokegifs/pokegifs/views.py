# import ipdb
import random
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
    giphy_response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={name}")
    giphy_body = json.loads(giphy_response.content)
    rand_num = random.randint(0, len(giphy_body['data'])-1)
    print(rand_num)
    print(len(giphy_body['data']))
    gif_url = giphy_body['data'][rand_num]['url']
    # ipdb.set_trace()
    # print(f"The location of the gif is: {gif_url}")
    return JsonResponse({'id': id, 'name': name, 'types': types, 'gif': gif_url})


def team(request):
    list_of_monsters = {}
    for num in range(1, 7):
        id = random.randint(1, 807)
        api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
        res = requests.get(api_url)
        body = json.loads(res.content)
        name = body["name"]
        types = []
        for type in body['types']:
            types.append(type['type']['name'])
        giphy_response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={name}")
        giphy_body = json.loads(giphy_response.content)
        if len(giphy_body['data']) == 0:
            gif_url = ''
        else:
            rand_num = random.randint(0, len(giphy_body['data'])-1)
            gif_url = giphy_body['data'][rand_num]['url']
        pokemon = {'id': id, 'name': name, 'types': types, 'gif': gif_url}
        print(pokemon)
        idx = f"pk{num}"
        list_of_monsters[idx] = pokemon
    print(list_of_monsters)

    return JsonResponse(list_of_monsters)
